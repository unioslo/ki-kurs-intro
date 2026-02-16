#!/usr/bin/env python3
"""
Update Canvas course pages from built HTML files.

Usage:
    export CANVAS_API_TOKEN="your_token_here"

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
from pathlib import Path
from bs4 import BeautifulSoup


# Configuration
CANVAS_URL = "https://uio.instructure.com"
COURSE_ID = "63248"
HTML_DIR = "../_build/html/episodes"


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
    print(f"{'Page ID':<12} {'Title':<50} {'URL':<30} {'Module':<30}")
    print("=" * 122)

    # Sort pages by module and position
    pages_sorted = sorted(pages, key=lambda p: (
        page_to_module.get(p['url'], {}).get('module_id', 999),
        page_to_module.get(p['url'], {}).get('position', 999)
    ))

    for page in pages_sorted:
        page_id = str(page.get('page_id', 'N/A'))
        title = page.get('title', 'Untitled')[:48]
        url = page.get('url', '')[:28]

        module_info = page_to_module.get(page['url'])
        if module_info:
            indent = "  " * module_info['indent']
            module_str = f"{indent}{module_info['module_name']}"[:28]
        else:
            module_str = "(not in module)"

        print(f"{page_id:<12} {title:<50} {url:<30} {module_str:<30}")

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


def extract_content(html_path):
    """Extract the main content from an HTML file, removing h1 tags and navigation."""
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

    return str(content)


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


def update_canvas_page(token, page_url_or_id, content, title=None, dry_run=False):
    """Update a Canvas page via API.

    Args:
        page_url_or_id: Either the page URL or page ID

    Returns: (success, actual_page_url)
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

    if dry_run:
        title_msg = f" (title: {title})" if title else ""
        print(f"  [DRY RUN] Would update: {page_url_or_id}{title_msg}")
        return True, page_url_or_id

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
                return False, None

            # Get the actual URL from Canvas response
            actual_url = response_data.get('url', page_url_or_id)

            title_msg = f" (title: {title})" if title else ""
            print(f"  ✓ Updated: {page_url_or_id}{title_msg}")
            print(f"    Canvas URL: {actual_url}")
            return True, actual_url
        except Exception as e:
            print(f"  Warning: Could not parse response: {e}")
            return True, page_url_or_id

    else:
        print(f"  ✗ Failed: {page_url_or_id} (Status: {response.status_code})")
        print(f"    Response: {response.text}")
        return False, None


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
        "--dry-run",
        action="store_true",
        help="Show what would be updated without making actual changes"
    )
    args = parser.parse_args()

    # Handle list-pages mode
    if args.list_pages:
        token = get_api_token()
        list_pages_with_modules(token)
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
    elif args.page_id:
        print("Error: --page-id requires --page to specify which HTML file to use")
        sys.exit(1)
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

        # Extract content
        content = extract_content(html_file)

        # Get Canvas page URL
        page_url = get_page_url(html_file.name)

        # Extract title from h1 tag
        title = extract_title(html_file)
        if title:
            print(f"  Extracted title: {title}")

        # Use page ID if provided, otherwise use page URL
        page_identifier = page_id_override if page_id_override else page_url

        # Update page
        page_updated, actual_page_url = update_canvas_page(token, page_identifier, content, title, args.dry_run)

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
