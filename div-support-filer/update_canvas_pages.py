#!/usr/bin/env python3
"""
Update Canvas course pages from built HTML files.

Usage:
    export CANVAS_API_TOKEN="your_token_here"

    # FIRST TIME SETUP: Generate mapping file from local HTML files
    python update_canvas_pages.py --generate-mapping

    # OR: Generate mapping from GitHub html-pages branch (no local build needed)
    python update_canvas_pages.py --generate-mapping --from-github

    # Deploy from GitHub (pull html-pages branch and upload to Canvas)
    python update_canvas_pages.py --from-github

    # List all pages with IDs, titles, and modules
    python update_canvas_pages.py --list-pages

    # Update all pages (content only)
    python update_canvas_pages.py

    # Update all pages and add them to modules
    python update_canvas_pages.py --add-to-modules

    # Update a single page by filename
    python update_canvas_pages.py --page episode1_0

    # Update a single page by Canvas page ID (stable when title changes)
    python update_canvas_pages.py --page-id 12345 --page episode1_0

    # Update all pages in a specific module and add to modules
    python update_canvas_pages.py --module 1 --add-to-modules

    # Dry run (no actual updates)
    python update_canvas_pages.py --dry-run
    python update_canvas_pages.py --module 2 --add-to-modules --dry-run

Mapping File:
    The script uses page_id_mapping.json to map filenames to Canvas page IDs.
    This allows you to use descriptive titles (which change the URL) while still
    reliably updating the correct pages. Run --generate-mapping to create/update it.

To get your Canvas API token:
1. Go to https://uio.instructure.com/profile/settings
2. Scroll to "Approved Integrations"
3. Click "+ New Access Token"
4. Generate and copy the token
"""

import os
import sys
import re
import argparse
import requests
import subprocess
import tempfile
import json
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup


# Configuration
CANVAS_URL = "https://uio.instructure.com"
COURSE_ID = "63248"
GITHUB_REPO = "https://github.com/unioslo/ki-kurs-intro.git"
HTML_BRANCH = "html-pages"

# Mapping file to store filename -> page_id relationships
MAPPING_FILE = Path(__file__).parent / "page_id_mapping.json"

# Simple path resolution: try current dir first, then parent
HTML_DIR = Path("_build/html/episodes")
if not HTML_DIR.exists():
    HTML_DIR = Path("../_build/html/episodes")


def get_api_token():
    """Get Canvas API token from environment variable."""
    token = os.environ.get("CANVAS_API_TOKEN")
    if not token:
        print("Error: CANVAS_API_TOKEN environment variable not set")
        print("\nTo set it, run:")
        print("  export CANVAS_API_TOKEN='your_token_here'")
        print("\nGet your token from: https://uio.instructure.com/profile/settings")
        sys.exit(1)
    return token


def load_page_mapping():
    """Load the page_id mapping from JSON file.

    Returns dict: {filename: {'page_id': ..., 'url': ..., 'title': ...}}
    """
    if not MAPPING_FILE.exists():
        return {}

    try:
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Could not load mapping file: {e}")
        return {}


def save_page_mapping(mapping):
    """Save the page_id mapping to JSON file.

    Args:
        mapping: dict {filename: {'page_id': ..., 'url': ..., 'title': ...}}
    """
    try:
        with open(MAPPING_FILE, 'w', encoding='utf-8') as f:
            json.dump(mapping, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved mapping to {MAPPING_FILE}")
    except Exception as e:
        print(f"Error: Could not save mapping file: {e}")


def generate_mapping_from_canvas(token, html_dir=None):
    """Generate filename -> page_id mapping by matching HTML files to Canvas pages.

    This function:
    1. Reads HTML files (episode1_0.html, episode1_1.html, etc.) from html_dir
    2. Extracts h1 title from each file
    3. Generates expected Canvas URL from title
    4. Matches against Canvas pages in modules by URL
    5. Creates mapping: episode1_1.html -> {page_id, url, title, module_id, module_name}
    6. Saves to JSON file

    Args:
        token: Canvas API token
        html_dir: Directory containing HTML files (default: local _build/html/episodes)
    """
    # Use provided html_dir or default to HTML_DIR
    if html_dir is None:
        html_dir = HTML_DIR
    else:
        html_dir = Path(html_dir)

    source_type = "GitHub html-pages branch" if html_dir != HTML_DIR else "local build"
    print(f"Generating page ID mapping from {source_type}...\n")

    # Check if HTML directory exists
    print(f"Looking for HTML files in: {html_dir.absolute()}")
    if not html_dir.exists():
        print(f"Error: HTML directory not found: {html_dir}")
        if html_dir == HTML_DIR:
            print("Please run 'make html' first to build the documentation")
        sys.exit(1)

    # Get all local HTML files
    html_files = sorted(html_dir.glob("episode*.html"))
    if not html_files:
        print(f"Error: No episode HTML files found in {HTML_DIR}")
        sys.exit(1)

    print(f"Found {len(html_files)} local HTML files")
    print(f"First few: {[f.name for f in html_files[:3]]}\n")

    # Get all pages
    all_pages = list_all_pages(token)
    pages_by_url = {p['url']: p for p in all_pages}

    # Get all modules and build set of page URLs that are in modules
    print("Fetching modules...")
    modules_map = get_modules(token)
    pages_in_modules = {}  # page_url -> {'module_id': ..., 'module_name': ...}
    module_names = {}

    # Fetch module names
    for module_position, module_id in modules_map.items():
        module_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/modules/{module_id}"
        response = requests.get(module_endpoint, headers={"Authorization": f"Bearer {token}"})
        if response.status_code == 200:
            module_data = response.json()
            module_names[module_id] = module_data.get('name', f'Module {module_position}')

    # Get pages from modules
    for module_position, module_id in modules_map.items():
        items = get_module_items(token, module_id)
        for item in items:
            if item.get('type') == 'Page':
                page_url = item.get('page_url')
                if page_url:
                    pages_in_modules[page_url] = {
                        'module_id': module_id,
                        'module_name': module_names.get(module_id, f'Module {module_position}')
                    }

    print(f"Found {len(pages_in_modules)} Canvas pages in modules")
    print(f"Sample module page URLs: {list(pages_in_modules.keys())[:5]}\n")

    # Now match local HTML files to Canvas pages
    mapping = {}
    matched_count = 0
    unmatched_count = 0

    print("Matching local HTML files to Canvas pages...")
    for html_file in html_files:
        # Extract h1 title from HTML file
        h1_title = extract_title(html_file)

        if not h1_title:
            print(f"  ✗ {html_file.name}: No h1 title found")
            unmatched_count += 1
            continue

        # Generate expected Canvas URL from title
        expected_url = title_to_canvas_url(h1_title)

        # Find all Canvas pages that match the expected URL (with or without digit suffix)
        # and are in modules - pick the one with highest suffix number
        matching_urls = []

        for canvas_url in pages_in_modules.keys():
            # Check if canvas_url matches expected_url with optional -\d+ suffix
            if canvas_url == expected_url:
                matching_urls.append((canvas_url, 0))  # No suffix = priority 0
            elif re.match(f"^{re.escape(expected_url)}-\\d+$", canvas_url):
                # Extract the suffix number
                match = re.match(f"^{re.escape(expected_url)}-(\\d+)$", canvas_url)
                if match:
                    suffix_num = int(match.group(1))
                    matching_urls.append((canvas_url, suffix_num))

        if not matching_urls:
            print(f"  ✗ {html_file.name}: No Canvas match in modules for '{h1_title}' (expected URL: {expected_url})")
            # Debug: show if similar URLs exist
            similar = [url for url in pages_in_modules.keys() if expected_url in url]
            if similar:
                print(f"     Similar URLs in modules: {similar[:3]}")
            unmatched_count += 1
            continue

        # Pick the URL with the highest suffix number
        matching_urls.sort(key=lambda x: x[1], reverse=True)
        canvas_url = matching_urls[0][0]

        # Get the Canvas page and module info
        canvas_page = pages_by_url.get(canvas_url)
        if not canvas_page:
            print(f"  ✗ {html_file.name}: Canvas page data not found for URL '{canvas_url}'")
            unmatched_count += 1
            continue

        module_info = pages_in_modules.get(canvas_url)

        # Create mapping
        page_id = canvas_page.get('page_id')
        canvas_title = canvas_page.get('title', '')

        mapping[html_file.name] = {
            'page_id': page_id,
            'url': canvas_url,
            'title': canvas_title,
            'module_id': module_info['module_id'],
            'module_name': module_info['module_name']
        }

        print(f"  ✓ {html_file.name} -> page_id: {page_id} | Module: {module_info['module_name']} | Title: {canvas_title}")
        matched_count += 1

    print(f"\n{'='*70}")
    print(f"Matched: {matched_count} | Unmatched: {unmatched_count} | Total: {len(html_files)}")
    print(f"{'='*70}\n")

    save_page_mapping(mapping)
    return mapping


def run_git_command(cmd, cwd=None, capture=True):
    """Run a git command and return output."""
    try:
        if capture:
            result = subprocess.run(
                cmd,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        else:
            subprocess.run(cmd, shell=True, cwd=cwd, check=True)
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error: {e.stderr if capture else e}")
        sys.exit(1)


def fetch_html_pages_branch(temp_dir):
    """Fetch the html-pages branch from GitHub to a temporary directory."""
    print(f"Fetching {HTML_BRANCH} branch from {GITHUB_REPO}...")
    print()

    # Clone only the html-pages branch (shallow clone for speed)
    run_git_command(
        f"git clone --depth 1 --branch {HTML_BRANCH} {GITHUB_REPO} {temp_dir}",
        capture=False
    )

    print(f"✓ Successfully fetched {HTML_BRANCH} branch\n")


def get_last_build_info(repo_dir):
    """Get information about the last build/commit."""
    # Get last commit date
    commit_date = run_git_command(
        "git log -1 --format=%cd --date=format:'%Y-%m-%d %H:%M:%S'",
        cwd=repo_dir
    )

    # Get last commit message
    commit_msg = run_git_command(
        "git log -1 --format=%s",
        cwd=repo_dir
    )

    # Get commit hash
    commit_hash = run_git_command(
        "git log -1 --format=%h",
        cwd=repo_dir
    )

    return {
        'date': commit_date,
        'message': commit_msg,
        'hash': commit_hash
    }


def ask_deploy_confirmation(build_info, html_files, dry_run=False, skip_confirmation=False):
    """Ask user to confirm deployment.

    Args:
        build_info: Dictionary with build information (date, hash, message)
        html_files: List of Path objects for HTML files to be deployed
        dry_run: Whether this is a dry run
        skip_confirmation: Skip confirmation prompt and return True automatically
    """
    if skip_confirmation:
        return True

    print("="*70)
    print("LAST BUILD INFORMATION:")
    print("="*70)
    print(f"  Date:    {build_info['date']}")
    print(f"  Commit:  {build_info['hash']}")
    print(f"  Message: {build_info['message']}")
    print("="*70)
    print()

    # Calculate time since build
    try:
        # Remove quotes from date string
        date_str = build_info['date'].strip("'")
        build_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        time_diff = datetime.now() - build_time

        minutes = int(time_diff.total_seconds() / 60)
        hours = int(minutes / 60)

        if hours > 0:
            time_ago = f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif minutes > 0:
            time_ago = f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        else:
            time_ago = "just now"

        print(f"This build was created {time_ago}.")
        print()
    except Exception:
        pass

    # Show files to be deployed
    print("="*70)
    print(f"FILES TO BE DEPLOYED ({len(html_files)}):")
    print("="*70)
    for html_file in html_files:
        print(f"  - {html_file.name}")
    print("="*70)
    print()

    # Different prompt based on dry-run mode
    if dry_run:
        prompt = "Preview these files? (DRY RUN - no changes will be made to Canvas) [yes/no]: "
    else:
        prompt = "Deploy these files to Canvas? [yes/no]: "

    while True:
        response = input(prompt).lower().strip()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            print("\nCancelled.")
            return False
        else:
            print("Please answer 'yes' or 'no'")


def create_page_id_mapping(token):
    """Create a mapping from episode filenames to Canvas page IDs.

    Only includes pages that are linked to modules, and picks the latest
    version if there are duplicates (e.g., avslutning, avslutning-2).

    Returns: (mapping, page_to_module)
    """
    print("Fetching Canvas pages and modules...")
    pages = list_all_pages(token)

    # Get all modules and build mapping of page URLs to modules
    modules_map = get_modules(token)
    pages_in_modules = set()
    page_to_module = {}  # page_url -> {'module_id': ..., 'module_name': ...}
    module_names = {}  # module_id -> module_name

    # Fetch module names
    for module_position, module_id in modules_map.items():
        module_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/modules/{module_id}"
        response = requests.get(module_endpoint, headers={"Authorization": f"Bearer {token}"})
        if response.status_code == 200:
            module_data = response.json()
            module_names[module_id] = module_data.get('name', f'Module {module_position}')

    for module_position, module_id in modules_map.items():
        items = get_module_items(token, module_id)
        for item in items:
            if item.get('type') == 'Page':
                page_url = item.get('page_url')
                if page_url:
                    pages_in_modules.add(page_url)
                    page_to_module[page_url] = {
                        'module_id': module_id,
                        'module_name': module_names.get(module_id, f'Module {module_position}')
                    }

    print(f"  Found {len(pages_in_modules)} pages linked to modules")
    print(f"  Processing all Canvas pages for episode matching...")

    # Create mapping: episode pattern -> page info
    # If duplicates exist, keep the one with highest page_id (latest)
    mapping = {}

    for page in pages:
        url = page.get('url', '')
        page_id = page.get('page_id')
        title = page.get('title', '')

        # Try to extract episode number from URL or title
        # Pattern: episode-X-Y or episodeX_Y
        patterns = [
            r'episode-?(\d+)-?(\d+)',  # episode-1-0, episode1-0
            r'episode.*?(\d+).*?(\d+)',  # more flexible
        ]

        match = None
        for pattern in patterns:
            match = re.search(pattern, url, re.IGNORECASE)
            if not match:
                match = re.search(pattern, title, re.IGNORECASE)
            if match:
                break

        if match:
            episode_num = int(match.group(1))
            sub_num = int(match.group(2))
            key = f"episode{episode_num}_{sub_num}"

            # If duplicate, keep the one with higher page_id (latest)
            module_info = page_to_module.get(url, {})
            module_id = module_info.get('module_id', 'N/A')
            module_name = module_info.get('module_name', 'N/A')

            if key in mapping:
                if page_id > mapping[key]['page_id']:
                    print(f"  Found newer version of {key}: {url} (page_id: {page_id})")
                    mapping[key] = {
                        'page_id': page_id,
                        'url': url,
                        'title': title,
                        'module_id': module_id,
                        'module_name': module_name
                    }
            else:
                mapping[key] = {
                    'page_id': page_id,
                    'url': url,
                    'title': title,
                    'module_id': module_id,
                    'module_name': module_name
                }

    print(f"✓ Mapped {len(mapping)} episode pages")
    print(f"  Episode keys found: {sorted(mapping.keys())[:10]}...")  # Show first 10 keys
    print()
    return mapping, page_to_module


def get_modules(token):
    """Fetch all modules for the course."""
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/modules"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        modules = response.json()
        # Create a dict mapping position to module_id
        module_map = {}
        for module in modules:
            position = module.get('position')
            module_id = module.get('id')
            if position and module_id:
                module_map[position] = module_id
        return module_map
    else:
        print(f"Warning: Failed to fetch modules (Status: {response.status_code})")
        print(f"Response: {response.text}")
        return {}


def get_page_by_id(token, page_id):
    """Fetch a Canvas page by its ID to get its current URL."""
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/pages/{page_id}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        page_data = response.json()
        return page_data.get('url'), page_data.get('title')
    else:
        print(f"Error: Failed to fetch page with ID {page_id} (Status: {response.status_code})")
        print(f"Response: {response.text}")
        return None, None


def list_all_pages(token):
    """Fetch all pages in the course."""
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/pages"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "per_page": 100  # Get up to 100 pages per request
    }

    all_pages = []
    while api_endpoint:
        response = requests.get(api_endpoint, headers=headers, params=params)

        if response.status_code == 200:
            pages = response.json()
            all_pages.extend(pages)

            # Check for pagination
            if 'next' in response.links:
                api_endpoint = response.links['next']['url']
                params = {}  # URL already includes params
            else:
                break
        else:
            print(f"Error: Failed to fetch pages (Status: {response.status_code})")
            print(f"Response: {response.text}")
            return []

    return all_pages


def get_module_items(token, module_id):
    """Fetch all items in a module."""
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/modules/{module_id}/items"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "per_page": 100
    }

    all_items = []
    while api_endpoint:
        response = requests.get(api_endpoint, headers=headers, params=params)

        if response.status_code == 200:
            items = response.json()
            all_items.extend(items)

            # Check for pagination
            if 'next' in response.links:
                api_endpoint = response.links['next']['url']
                params = {}
            else:
                break
        else:
            return []

    return all_items


def list_pages_with_modules(token):
    """List all pages with their IDs, titles, URLs, and which module they belong to."""
    print("Fetching pages and modules...\n")

    # Load page mapping to show HTML filenames
    page_mapping = load_page_mapping()
    # Create reverse lookup: page_id -> filename
    page_id_to_file = {}
    if page_mapping:
        for filename, info in page_mapping.items():
            page_id_to_file[info['page_id']] = filename
        print(f"Loaded {len(page_mapping)} file mappings\n")

    # Get all pages
    pages = list_all_pages(token)
    if not pages:
        print("No pages found.")
        return

    # Get all modules
    modules_map = get_modules(token)

    # Build a mapping of page_url -> module info
    page_to_module = {}
    module_names = {}

    for position, module_id in modules_map.items():
        # Get module details
        module_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/modules/{module_id}"
        response = requests.get(module_endpoint, headers={"Authorization": f"Bearer {token}"})
        if response.status_code == 200:
            module_data = response.json()
            module_names[module_id] = module_data.get('name', f'Module {position}')

        # Get items in this module
        items = get_module_items(token, module_id)
        for item in items:
            if item.get('type') == 'Page':
                page_url = item.get('page_url')
                if page_url:
                    page_to_module[page_url] = {
                        'module_id': module_id,
                        'module_name': module_names.get(module_id, f'Module {position}'),
                        'position': item.get('position'),
                        'indent': item.get('indent', 0)
                    }

    # Print header
    print(f"{'Page ID':<12} {'Title':<35} {'URL':<45} {'HTML File':<20} {'Created':<20} {'Updated':<20} {'Mod ID':<10} {'Module':<30}")
    print("=" * 207)

    # Sort pages by module and position
    pages_sorted = sorted(pages, key=lambda p: (
        page_to_module.get(p['url'], {}).get('module_id', 999),
        page_to_module.get(p['url'], {}).get('position', 999)
    ))

    for page in pages_sorted:
        page_id = str(page.get('page_id', 'N/A'))
        title = page.get('title', 'Untitled')[:33]
        url = page.get('url', '')[:43]

        # Look up HTML filename from mapping
        html_file = page_id_to_file.get(int(page_id), 'N/A') if page_id.isdigit() else 'N/A'
        if html_file != 'N/A':
            html_file = html_file[:18]  # Truncate if too long

        # Format timestamps
        created_at = page.get('created_at', 'N/A')
        updated_at = page.get('updated_at', 'N/A')

        # Parse and format timestamps if they exist
        if created_at != 'N/A' and 'T' in str(created_at):
            try:
                from datetime import datetime as dt
                parsed = dt.fromisoformat(created_at.replace('Z', '+00:00'))
                created_at = parsed.strftime('%Y-%m-%d %H:%M')
            except:
                pass

        if updated_at != 'N/A' and 'T' in str(updated_at):
            try:
                from datetime import datetime as dt
                parsed = dt.fromisoformat(updated_at.replace('Z', '+00:00'))
                updated_at = parsed.strftime('%Y-%m-%d %H:%M')
            except:
                pass

        module_info = page_to_module.get(page['url'])
        if module_info:
            indent = "  " * module_info['indent']
            module_str = f"{indent}{module_info['module_name']}"[:28]
            mod_id = str(module_info['module_id'])
        else:
            module_str = "(not in module)"
            mod_id = "N/A"

        print(f"{page_id:<12} {title:<35} {url:<45} {html_file:<20} {str(created_at):<20} {str(updated_at):<20} {mod_id:<10} {module_str:<30}")

    print(f"\nTotal: {len(pages)} pages")


def add_page_to_module(token, module_id, page_url, title, position, indent, dry_run=False):
    """Add a page to a module."""
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/modules/{module_id}/items"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "module_item[title]": title,
        "module_item[type]": "Page",
        "module_item[page_url]": page_url,
        "module_item[position]": position,
        "module_item[indent]": indent
    }


    print(f"Attempting to update page url: {page_url} with api_endpoint: {api_endpoint}")
    if dry_run:
        print(f"    [DRY RUN] Would add to module {module_id}: position={position}, indent={indent}")
        return True

    response = requests.post(api_endpoint, headers=headers, data=data)

    if response.status_code in [200, 201]:
        # Check if response contains an error message
        try:
            response_data = response.json()
            if "message" in response_data or "errors" in response_data:
                # Error in response body despite success status
                print(f"    ✗ Failed to add to module (Status: {response.status_code})")
                print(f"      Response: {response.text}")
                return False
        except:
            pass  # Not JSON or no error, continue as success

        print(f"    ✓ Added to module {module_id}: position={position}, indent={indent}")
        return True
    else:
        print(f"    ✗ Failed to add to module (Status: {response.status_code})")
        print(f"      Response: {response.text}")
        return False


def upload_image_to_canvas(token, image_path):
    """Upload an image file to Canvas following the official file upload workflow.

    Workflow:
    1. POST to /api/v1/courses/:course_id/files to get upload URL and params
    2. POST the actual file to the upload_url with upload_params
    3. Follow redirect to confirm and get file object with ID

    Args:
        token: Canvas API token
        image_path: Path to the image file

    Returns:
        Tuple of (file_id, preview_url) or (None, None) if upload fails
    """
    import mimetypes

    image_path = Path(image_path)

    if not image_path.exists():
        print(f"  Warning: Image file not found: {image_path}")
        return None, None

    # Determine MIME type
    mime_type, _ = mimetypes.guess_type(str(image_path))
    if not mime_type:
        mime_type = 'application/octet-stream'

    # Step 1: Notify Canvas and obtain upload token
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/files"
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "name": image_path.name,
        "size": image_path.stat().st_size,
        "content_type": mime_type,
        "parent_folder_path": "course_images",  # Store images in dedicated folder
        "on_duplicate": "overwrite"  # Overwrite if same filename exists
    }

    response = requests.post(api_endpoint, headers=headers, data=payload)

    if response.status_code not in [200, 201]:
        print(f"  Warning: Failed to initiate image upload for {image_path.name}")
        print(f"  Status: {response.status_code}, Response: {response.text}")
        return None, None

    upload_info = response.json()
    upload_url = upload_info.get('upload_url')
    upload_params = upload_info.get('upload_params', {})

    if not upload_url:
        print(f"  Warning: No upload URL received for {image_path.name}")
        return None, None

    # Step 2: Upload the actual file
    # Important: Do NOT send the access token with this request
    # File must be the last field in the multipart form
    with open(image_path, 'rb') as f:
        files = {'file': (image_path.name, f, mime_type)}
        upload_response = requests.post(upload_url, data=upload_params, files=files)

    # Step 3: Follow redirect to confirm upload success
    if upload_response.status_code in [301, 302, 303]:
        # Follow redirect with authenticated GET request
        location = upload_response.headers.get('Location')
        if location:
            confirm_headers = {"Authorization": f"Bearer {token}"}
            upload_response = requests.get(location, headers=confirm_headers)

    if upload_response.status_code not in [200, 201]:
        print(f"  Warning: Failed to upload image {image_path.name}")
        print(f"  Status: {upload_response.status_code}, Response: {upload_response.text}")
        return None, None

    # Get file info from response
    try:
        file_info = upload_response.json()
        file_id = file_info.get('id')
        preview_url = f"{CANVAS_URL}/courses/{COURSE_ID}/files/{file_id}/preview"

        print(f"    ✓ Uploaded: {image_path.name} (file_id: {file_id})")
        return file_id, preview_url
    except Exception as e:
        print(f"  Warning: Could not parse upload response for {image_path.name}: {e}")
        return None, None


def process_images_in_html(token, html_content, html_path, dry_run=False):
    """Find all images in HTML, upload to Canvas, and update img tags with Canvas URLs.

    Args:
        token: Canvas API token
        html_content: HTML content as string
        html_path: Path to the HTML file (used to resolve relative image paths)
        dry_run: If True, don't actually upload images

    Returns:
        Updated HTML content with Canvas image URLs
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    html_path = Path(html_path)

    # Find all img tags
    img_tags = soup.find_all('img')

    if not img_tags:
        return html_content

    print(f"  Found {len(img_tags)} image(s) to process")

    uploaded_count = 0
    skipped_count = 0

    for img in img_tags:
        src = img.get('src')
        if not src:
            continue

        # Skip if already a Canvas URL
        if 'instructure.com' in src:
            print(f"    • Skipping (already Canvas URL): {src}")
            skipped_count += 1
            continue

        # Resolve relative path
        # Images are typically referenced as ../images/filename.png or ../_images/filename.png
        if src.startswith('../'):
            # Resolve relative to HTML file directory
            image_path = (html_path.parent / src).resolve()
        elif src.startswith('/'):
            # Absolute path
            image_path = Path(src)
        else:
            # Relative path without ../
            image_path = (html_path.parent / src).resolve()

        if not image_path.exists():
            print(f"    ✗ Image not found: {src}")
            print(f"      Resolved to: {image_path}")
            continue

        # Get alt text
        alt_text = img.get('alt', image_path.name)

        if dry_run:
            print(f"    • [DRY RUN] Would upload: {src}")
            print(f"      Local path: {image_path}")
            uploaded_count += 1
            continue

        # Upload image to Canvas
        print(f"    • Uploading: {src}")
        print(f"      Local path: {image_path}")
        file_id, preview_url = upload_image_to_canvas(token, image_path)

        if file_id and preview_url:
            uploaded_count += 1
            print(f"      Canvas URL: {preview_url}")

            # Preserve existing width/height if set
            width = img.get('width') or img.get('style', '').split('width:')[-1].split(';')[0].strip()
            height = img.get('height') or img.get('style', '').split('height:')[-1].split(';')[0].strip()

            # Update img tag with Canvas URL format
            img['src'] = preview_url
            img['id'] = str(file_id)  # Add id attribute with file_id
            img['data-api-endpoint'] = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/files/{file_id}"
            img['data-api-returntype'] = "File"

            # Preserve or add alt text
            if alt_text:
                img['alt'] = alt_text
                img['data-ally-user-updated-alt'] = alt_text

            # Preserve width/height if they existed
            if width and 'width' in img.attrs:
                img['width'] = width
            if height and 'height' in img.attrs:
                img['height'] = height

            # Remove parent <a> tag if it's wrapping the image (to prevent clickable images)
            parent = img.parent
            if parent and parent.name == 'a' and 'image-reference' in parent.get('class', []):
                # Replace the <a> tag with just the <img> tag
                parent.replace_with(img)
        else:
            print(f"      ✗ Upload failed")

    # Summary
    if uploaded_count > 0 or skipped_count > 0:
        print(f"  Image summary: {uploaded_count} uploaded, {skipped_count} skipped")

    return str(soup)


def extract_content(html_path, token=None, dry_run=False):
    """Extract the main content from an HTML file, removing h1 tags and navigation.

    Args:
        html_path: Path to the HTML file
        token: Canvas API token (optional, needed for image uploads)
        dry_run: If True, don't actually upload images

    Returns:
        HTML content string with processed images
    """
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find the main content section
    # Adjust this selector based on your Sphinx theme
    content = soup.find('section')
    if not content:
        # Fallback to body if section not found
        content = soup.find('body')

    if not content:
        content = soup

    # Remove all h1 tags to avoid duplication (Canvas adds title automatically)
    for h1 in content.find_all('h1'):
        h1.decompose()

    # Remove navigation buttons (Forrige/Neste)
    for nav in content.find_all('div', class_='page-navigation'):
        nav.decompose()

    content_html = str(content)

    # Process images if token is provided
    if token:
        content_html = process_images_in_html(token, content_html, html_path, dry_run)

    return content_html


def extract_title(html_path):
    """Extract the title from an HTML file.

    Looks for the first h1 tag in the content section.
    """
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Try to find h1 in section first
    section = soup.find('section')
    if section:
        h1 = section.find('h1')
        if h1:
            return h1.get_text().strip()

    # Fallback to any h1
    h1 = soup.find('h1')
    if h1:
        return h1.get_text().strip()

    # Fallback to title tag
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.get_text().strip()

    return None


def get_page_url(filename):
    """Convert filename to Canvas page URL.

    Example: episode1_0.html -> episode-1-0
    """
    # Remove .html extension
    name = filename.replace('.html', '')
    # Replace underscores with hyphens
    name = name.replace('_', '-')
    return name


def title_to_canvas_url(title):
    """Convert a title to expected Canvas URL format.

    Canvas generates URLs by:
    - Replacing Norwegian characters: æ→ae, ø→o, å→a
    - Lowercasing
    - Replacing spaces with hyphens
    - Removing/replacing special characters
    """
    import re

    # Convert to lowercase first
    url = title.lower()

    # Replace Norwegian characters specifically
    url = url.replace('æ', 'ae')
    url = url.replace('ø', 'o')
    url = url.replace('å', 'a')

    # Remove parentheses and other special chars
    url = re.sub(r'[^\w\s-]', '', url)  # Remove non-word chars except spaces and hyphens
    url = re.sub(r'[-\s]+', '-', url)   # Replace spaces and multiple hyphens with single hyphen

    # Remove leading/trailing hyphens
    url = url.strip('-')

    return url


def generate_title_from_filename(filename):
    """Generate a Canvas page title from filename.

    This creates a stable title that matches the URL format.
    Example: episode1_0.html -> Episode1-0 (URL: episode1-0)
             episode2_3.html -> Episode2-3 (URL: episode2-3)
    """
    import re
    # Remove .html extension
    name = filename.replace('.html', '')

    # Extract episode numbers: episode1_0 -> (1, 0)
    match = re.match(r'episode(\d+)_(\d+)', name)
    if match:
        major = match.group(1)
        minor = match.group(2)
        # Match the URL format: Episode1-0
        return f"Episode{major}-{minor}"

    # Fallback: just clean up the name
    return name.replace('_', '-').title()


def update_canvas_page(token, page_url_or_id, content, title=None, new_url=None, dry_run=False):
    """Update a Canvas page via API.

    Args:
        page_url_or_id: Either the page URL or page ID
        content: Page body content
        title: Optional new title
        new_url: Optional new URL (e.g., "episode-1-1")
        dry_run: If True, don't make actual changes

    Returns: (success, actual_page_url, updated_at)
    """
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/pages/{page_url_or_id}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "wiki_page": {
            "body": content
        }
    }

    # Add title if provided
    if title:
        data["wiki_page"]["title"] = title

    # Add URL if provided
    if new_url:
        data["wiki_page"]["url"] = new_url

    if dry_run:
        title_msg = f" (title: {title})" if title else ""
        # Calculate expected URL from title if not explicitly set
        if new_url:
            expected_url = new_url
        elif title:
            expected_url = title_to_canvas_url(title)
        else:
            expected_url = page_url_or_id
        url_msg = f" (new URL: {expected_url})" if expected_url else ""
        print(f"  [DRY RUN] Would update: {page_url_or_id}{title_msg}{url_msg}")
        return True, expected_url, None

    response = requests.put(api_endpoint, headers=headers, json=data)

    # Check for successful response
    if response.status_code == 200:
        # Also check if response contains an error message
        try:
            response_data = response.json()
            if "message" in response_data or "errors" in response_data:
                # Error in response body despite 200 status
                print(f"  ✗ Failed: {page_url_or_id} (Status: {response.status_code})")
                print(f"    Response: {response.text}")
                return False, None, None

            # Get the actual URL and timestamp from Canvas response
            actual_url = response_data.get('url', page_url_or_id)
            updated_at = response_data.get('updated_at', 'N/A')

            title_msg = f" (title: {title})" if title else ""
            print(f"  ✓ Updated: {page_url_or_id}{title_msg}")
            print(f"    Canvas URL: {actual_url}")
            return True, actual_url, updated_at
        except Exception as e:
            print(f"  Warning: Could not parse response: {e}")
            return True, page_url_or_id, None

    else:
        print(f"  ✗ Failed: {page_url_or_id} (Status: {response.status_code})")
        print(f"    Response: {response.text}")
        return False, None, None


def main():
    """Main function to update all Canvas pages."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Update Canvas course pages from built HTML files"
    )
    parser.add_argument(
        "--page",
        type=str,
        help="Update only a single page by filename (e.g., episode-1-0 or episode1_0.html)"
    )
    parser.add_argument(
        "--page-id",
        type=str,
        help="Update only a single page by Canvas page ID (e.g., 12345). Takes precedence over --page."
    )
    parser.add_argument(
        "--module",
        type=int,
        help="Update only pages from a specific module/episode (e.g., 1 for episode1_X)"
    )
    parser.add_argument(
        "--add-to-modules",
        action="store_true",
        help="Add pages to Canvas modules after updating (default: only update page content)"
    )
    parser.add_argument(
        "--list-pages",
        action="store_true",
        help="List all pages with their IDs, titles, URLs, and modules (does not update anything)"
    )
    parser.add_argument(
        "--from-github",
        action="store_true",
        help="Fetch HTML from GitHub html-pages branch instead of using local _build/html files"
    )
    parser.add_argument(
        "--generate-mapping",
        action="store_true",
        help="Generate page_id_mapping.json from Canvas pages (run this once or when pages change)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be updated without making actual changes"
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip confirmation prompt and proceed automatically"
    )
    args = parser.parse_args()

    # Validate argument dependencies
    if args.page_id and not args.page:
        parser.error("--page-id requires --page to specify which HTML file to use")

    # Handle generate-mapping mode
    if args.generate_mapping:
        token = get_api_token()

        # Check if --deploy flag is also set (generate from GitHub instead of local)
        if args.from_github:
            print("\n" + "="*70)
            print("GENERATE MAPPING FROM GITHUB")
            print("="*70 + "\n")

            # Create temporary directory for git clone in /tmp
            with tempfile.TemporaryDirectory(dir='/tmp') as temp_dir:
                print(f"Using temporary directory: {temp_dir}\n")

                # Fetch html-pages branch
                fetch_html_pages_branch(temp_dir)

                # Get last build info
                build_info = get_last_build_info(temp_dir)
                print(f"\nUsing HTML files from:")
                print(f"  Branch: {HTML_BRANCH}")
                print(f"  Last commit: {build_info.get('commit_hash', 'N/A')}")
                print(f"  Build time: {build_info.get('build_time', 'N/A')}")
                print()

                # Generate mapping from GitHub HTML files
                episodes_dir = Path(temp_dir) / "html" / "episodes"

                if not episodes_dir.exists():
                    print(f"Error: Episodes directory not found: {episodes_dir}")
                    sys.exit(1)

                generate_mapping_from_canvas(token, html_dir=episodes_dir)
        else:
            # Generate from local HTML files
            generate_mapping_from_canvas(token)

        return

    # Handle list-pages mode
    if args.list_pages:
        token = get_api_token()
        list_pages_with_modules(token)
        return

    # Handle deploy mode
    if args.from_github:
        print("\n" + "="*70)
        print("CANVAS DEPLOYMENT FROM GITHUB")
        if args.dry_run:
            print("*** DRY RUN MODE - NO CHANGES WILL BE MADE ***")
        print("="*70 + "\n")

        token = get_api_token()

        # Create temporary directory for git clone in /tmp
        with tempfile.TemporaryDirectory(dir='/tmp') as temp_dir:
            print(f"Using temporary directory: {temp_dir}\n")

            # Step 1: Fetch html-pages branch
            fetch_html_pages_branch(temp_dir)

            # Step 2: Get last build info
            build_info = get_last_build_info(temp_dir)

            # Step 3: Determine which files to process (before asking for confirmation)
            episodes_dir = Path(temp_dir) / "html" / "episodes"

            if not episodes_dir.exists():
                print(f"Error: Episodes directory not found: {episodes_dir}")
                sys.exit(1)

            # Determine which files to process
            if args.page:
                # Single page mode - convert page name to filename if needed
                page_name = args.page
                if not page_name.endswith('.html'):
                    # Convert episode-1-0 or episode1_0 to episode1_0.html
                    page_name = page_name.replace('-', '_') + '.html'

                html_file = episodes_dir / page_name
                if not html_file.exists():
                    print(f"Error: HTML file not found in GitHub: {html_file}")
                    print(f"Available files in {episodes_dir}:")
                    for f in sorted(episodes_dir.glob("episode*.html")):
                        print(f"  - {f.name}")
                    sys.exit(1)

                html_files = [html_file]
            else:
                # Get all episode HTML files
                html_files = sorted(episodes_dir.glob("episode*.html"))

                if not html_files:
                    print(f"No episode HTML files found in {episodes_dir}")
                    sys.exit(1)

            # Step 4: Ask for confirmation (showing which files will be deployed)
            if not ask_deploy_confirmation(build_info, html_files, args.dry_run, args.yes):
                return

            if args.dry_run:
                print("\nProceeding with preview (DRY RUN)...\n")
            else:
                print("\nProceeding with deployment...\n")

            # Load page ID mapping from file (includes module info)
            print("Loading page ID mapping file...")
            page_mapping = load_page_mapping()

            if not page_mapping:
                print(f"Warning: No mapping file found at {MAPPING_FILE}")
                print("Run with --generate-mapping first to create the mapping file")
                print("Continuing anyway, will use URL-based fallback...\n")
            else:
                print(f"✓ Loaded {len(page_mapping)} page mappings\n")

            # Track deployment results for summary table
            deploy_results = []

            # Process each file
            success_count = 0
            fail_count = 0

            for html_file in html_files:
                print(f"Processing: {html_file.name}")

                # Extract content (includes image processing and upload)
                content = extract_content(html_file, token=token, dry_run=args.dry_run)

                # Extract title from h1 (use descriptive title)
                title = extract_title(html_file)
                if title:
                    print(f"  Title: {title}")

                # Try to find the Canvas page ID from mapping file
                page_info = page_mapping.get(html_file.name)

                if page_info:
                    # Use page ID from mapping file (includes module info)
                    page_identifier = page_info['page_id']
                    old_url = page_info['url']
                    module_id = page_info.get('module_id', 'N/A')
                    module_name = page_info.get('module_name', 'N/A')
                    print(f"  Canvas page ID: {page_identifier}")
                    print(f"  Current URL: {old_url}")
                    if module_name != 'N/A':
                        print(f"  Module: {module_name}")
                else:
                    # Fallback to URL-based matching
                    page_identifier = get_page_url(html_file.name)
                    old_url = "N/A"
                    module_id = 'N/A'
                    module_name = 'N/A'
                    print(f"  Warning: No page ID found in mapping for '{html_file.name}'")
                    print(f"    Using fallback URL: {page_identifier}")
                    print(f"    (Run --generate-mapping to update the mapping file)")

                # Update page (without URL field - let Canvas auto-generate from title)
                page_updated, actual_page_url, updated_at = update_canvas_page(
                    token,
                    page_identifier,
                    content,
                    title,
                    None,  # Don't set URL - let Canvas auto-generate
                    args.dry_run
                )

                # Track result for summary table
                new_url = actual_page_url if actual_page_url else "N/A"
                timestamp = updated_at if updated_at else "N/A"

                deploy_results.append({
                    'file': html_file.name,
                    'page_id': page_info['page_id'] if page_info else 'N/A',
                    'old_url': old_url,
                    'new_url': new_url,
                    'module_id': module_id,
                    'module_name': module_name,
                    'timestamp': timestamp,
                    'success': page_updated
                })

                if page_updated:
                    success_count += 1
                else:
                    fail_count += 1

                print()

            # Summary
            print("="*220)
            print("DEPLOYMENT SUMMARY:")
            print("="*220)
            print(f"{'File':<20} {'Page ID':<10} {'Old URL':<50} {'Expected URL':<50} {'Module ID':<12} {'Module Name':<30} {'Updated At':<20} {'Status':<10}")
            print("-"*220)

            for result in deploy_results:
                status = "✓ Success" if result['success'] else "✗ Failed"
                # Format timestamp to be more readable if it's in ISO format
                timestamp = result['timestamp']
                if timestamp != "N/A" and 'T' in str(timestamp):
                    try:
                        # Parse and reformat ISO timestamp
                        from datetime import datetime as dt
                        parsed = dt.fromisoformat(timestamp.replace('Z', '+00:00'))
                        timestamp = parsed.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        pass  # Keep original if parsing fails

                module_name_truncated = str(result['module_name'])[:28]  # Truncate if too long
                print(f"{result['file']:<20} {str(result['page_id']):<10} {result['old_url']:<50} "
                      f"{result['new_url']:<50} {str(result['module_id']):<12} {module_name_truncated:<30} "
                      f"{str(timestamp):<20} {status:<10}")

            print("="*220)
            print(f"Total: {len(html_files)} | Successful: {success_count} | Failed: {fail_count}")
            print("="*220)

            if fail_count == 0:
                print("\n✓ Deployment completed successfully!")
            else:
                print("\n✗ Deployment completed with errors.")

        return

    if args.dry_run:
        print("Running in DRY RUN mode - no actual updates will be made\n")

    # Get API token
    token = get_api_token()

    # Fetch modules only if --add-to-modules is set
    modules = {}
    if args.add_to_modules:
        print("Fetching modules...")
        modules = get_modules(token)
        if modules:
            print(f"Found {len(modules)} modules")
            for pos, mod_id in sorted(modules.items()):
                print(f"  Module {pos}: ID {mod_id}")
        else:
            print("Warning: No modules found or failed to fetch modules")
        print()
    else:
        print("Module addition disabled (use --add-to-modules to enable)\n")

    # Check if HTML directory exists
    html_dir = Path(HTML_DIR)
    if not html_dir.exists():
        print(f"Error: HTML directory not found: {HTML_DIR}")
        print("Please run 'make html' first to build the documentation")
        sys.exit(1)

    # Load page ID mapping file (for page IDs and module info)
    print("Loading page ID mapping file...")
    page_mapping = load_page_mapping()

    if not page_mapping:
        print(f"Warning: No mapping file found at {MAPPING_FILE}")
        print("Run with --generate-mapping first to create the mapping file")
        print("Continuing anyway, will use URL-based fallback...\n")
    else:
        print(f"✓ Loaded {len(page_mapping)} page mappings\n")

    # Handle page ID mode
    page_id_override = None
    if args.page_id:
        print(f"Fetching page with ID {args.page_id}...")
        current_url, current_title = get_page_by_id(token, args.page_id)
        if not current_url:
            sys.exit(1)
        print(f"  Current URL: {current_url}")
        print(f"  Current title: {current_title}")
        page_id_override = args.page_id
        print()

    # Determine which files to process
    if args.page_id and args.page:
        # Page ID with specific HTML file
        page_name = args.page
        if not page_name.endswith('.html'):
            # Convert episode-1-0 to episode1_0.html
            page_name = page_name.replace('-', '_') + '.html'

        html_file = html_dir / page_name
        if not html_file.exists():
            print(f"Error: HTML file not found: {html_file}")
            sys.exit(1)

        html_files = [html_file]
        print(f"Single page mode (using page ID {args.page_id}): {html_file.name}\n")
    elif args.page:
        # Single page mode by filename
        # Convert page URL to filename if needed
        page_name = args.page
        if not page_name.endswith('.html'):
            # Convert episode-1-0 to episode1_0.html
            page_name = page_name.replace('-', '_') + '.html'

        html_file = html_dir / page_name
        if not html_file.exists():
            print(f"Error: HTML file not found: {html_file}")
            sys.exit(1)

        html_files = [html_file]
        print(f"Single page mode: {html_file.name}\n")
    elif args.module:
        # Module mode - filter by episode number
        html_files = sorted(html_dir.glob(f"episode{args.module}_*.html"))

        if not html_files:
            print(f"No episode HTML files found for module {args.module} in {HTML_DIR}")
            sys.exit(1)

        print(f"Module {args.module} mode: Found {len(html_files)} HTML files to process\n")
    else:
        # All pages mode
        html_files = sorted(html_dir.glob("episode*.html"))

        if not html_files:
            print(f"No episode HTML files found in {HTML_DIR}")
            sys.exit(1)

        print(f"Found {len(html_files)} HTML files to process\n")

    # Process each file
    success_count = 0
    fail_count = 0

    # Track position within each module
    module_positions = {}

    for html_file in html_files:
        print(f"Processing: {html_file.name}")

        # Extract content (includes image processing and upload)
        content = extract_content(html_file, token=token, dry_run=args.dry_run)

        # Extract title from h1 tag (descriptive title)
        title = extract_title(html_file)
        if title:
            print(f"  Title: {title}")

        # Try to find page info from mapping file
        page_info = page_mapping.get(html_file.name)

        if page_info:
            # Use page ID from mapping file
            page_identifier = page_id_override if page_id_override else page_info['page_id']
            print(f"  Page ID: {page_info['page_id']}")
            print(f"  Module: {page_info.get('module_name', 'N/A')} (ID: {page_info.get('module_id', 'N/A')})")
        else:
            # Fallback to URL-based identifier
            page_url = get_page_url(html_file.name)
            page_identifier = page_id_override if page_id_override else page_url
            print(f"  Warning: No mapping found for {html_file.name}, using URL: {page_url}")

        # Update page (let Canvas auto-generate URL from title)
        page_updated, actual_page_url, _ = update_canvas_page(token, page_identifier, content, title, None, args.dry_run)

        if page_updated:
            success_count += 1

            # Add to module if modules are available
            if modules and actual_page_url:
                # Parse episode number from filename (e.g., episode1_0 -> module 1)
                filename_base = html_file.stem  # e.g., episode1_0
                match = re.match(r'episode(\d+)_(\d+)', filename_base)
                if match:
                    episode_num = int(match.group(1))  # 1, 2, 3, etc.
                    sub_num = int(match.group(2))      # 0, 1, 2, etc.

                    # Get module ID for this episode
                    module_id = modules.get(episode_num)

                    if module_id:
                        # Determine indent: 0 for _0 pages, 1 for others
                        indent = 0 if sub_num == 0 else 1

                        # Get position within this module
                        if episode_num not in module_positions:
                            module_positions[episode_num] = 1
                        position = module_positions[episode_num]
                        module_positions[episode_num] += 1

                        # Add page to module using the actual Canvas URL
                        add_page_to_module(token, module_id, actual_page_url, title or actual_page_url,
                                          position, indent, args.dry_run)
                    else:
                        print(f"    Warning: No module found for episode {episode_num}")
        else:
            fail_count += 1

    # Summary
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Successful: {success_count}")
    print(f"  Failed: {fail_count}")
    print(f"  Total: {len(html_files)}")

    if args.dry_run:
        print("\nThis was a DRY RUN. Run without --dry-run to actually update pages.")


if __name__ == "__main__":
    main()
