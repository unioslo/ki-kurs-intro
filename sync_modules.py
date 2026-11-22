#!/usr/bin/env python3
"""
Copy modules AND page items from a source Canvas course to a target course.

Used to mirror the Norwegian course (63248) module structure into the
English course (65902), including translated module names and page ordering.

Usage:
    python sync_modules.py --source 63248 --target 65902 --dry-run
    python sync_modules.py --source 63248 --target 65902
    python sync_modules.py --source 63248 --target 65902 --yes

Requires: CANVAS_API_TOKEN environment variable set.
"""

import argparse
import json
import os
import sys
from pathlib import Path
import requests

CANVAS_URL = "https://uio.instructure.com"

MODULE_NAME_TRANSLATIONS = {
    'Introduksjon til "KI-språket"': "Introduction to the language of AI",
    "Introduksjon til \"KI-språket\"": "Introduction to the language of AI",
    "Store språkmodeller": "Large language models",
    "Instruksjoner: Bli god på KI!": "Instructions: Get good at AI!",
    "Ansvarlig og bærekraftig bruk av KI": "Responsible and sustainable use of AI",
    "KI-tjenester ved UiO": "AI services at UiO",
    "Oppsummering og veien videre": "Summary and the way forward",
}


def get_api_token():
    token = os.environ.get("CANVAS_API_TOKEN")
    if not token:
        print("Error: CANVAS_API_TOKEN environment variable not set")
        sys.exit(1)
    return token


def _load_mapping(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: Could not load {path}: {e}")
        return {}


def get_modules(token, course_id):
    endpoint = f"{CANVAS_URL}/api/v1/courses/{course_id}/modules?per_page=100"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return {mod.get('position'): mod.get('id') for mod in response.json()
                if mod.get('position') and mod.get('id')}
    print(f"Warning: Failed to fetch modules from course {course_id}")
    return {}


def get_module_names(token, course_id):
    """Return a dict of {position: name} for all modules in a course."""
    endpoint = f"{CANVAS_URL}/api/v1/courses/{course_id}/modules?per_page=100"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return {mod.get('position'): mod.get('name', '') for mod in response.json()
                if mod.get('position')}
    print(f"Warning: Failed to fetch modules from course {course_id}")
    return {}


def rename_module(token, course_id, module_id, new_name):
    endpoint = f"{CANVAS_URL}/api/v1/courses/{course_id}/modules/{module_id}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {"module": {"name": new_name}}
    response = requests.put(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        return True
    print(f"Warning: Failed to rename module {module_id} (status {response.status_code})")
    return False


def get_module_items(token, course_id, module_id):
    endpoint = f"{CANVAS_URL}/api/v1/courses/{course_id}/modules/{module_id}/items?per_page=100"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    print(f"Warning: Failed to fetch items for module {module_id}")
    return []


def create_module(token, course_id, name, position):
    endpoint = f"{CANVAS_URL}/api/v1/courses/{course_id}/modules"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {"module": {"name": name, "position": position, "published": True}}
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code in [200, 201]:
        return response.json().get('id')
    print(f"Failed to create module '{name}': {response.status_code}")
    return None


def get_existing_page_urls(token, course_id, module_id):
    """Return a set of page_url slugs already present in a module."""
    items = get_module_items(token, course_id, module_id)
    return {
        item['page_url']
        for item in items
        if item.get('type') == 'Page' and item.get('page_url')
    }


def fetch_target_pages(token, course_id):
    """Fetch all wiki pages in a course and return a dict of normalized title → page data.

    This is used to match pages by title (robust against stale page_ids in mapping files).
    """
    endpoint = f"{CANVAS_URL}/api/v1/courses/{course_id}/pages?per_page=100"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        print(f"Warning: Failed to fetch pages from course {course_id}")
        return {}

    pages = response.json()
    result = {}
    for p in pages:
        title = p.get('title', '')
        url = p.get('url', '')
        if title and url:
            result[_normalize_title(title)] = {"url": url, "page_id": p.get('id')}
    return result


def _normalize_title(title):
    """Normalize a page title for matching: lowercase, strip, replace smart quotes."""
    # Replace curly/smart quotes with straight quotes for matching
    title = title.replace('\u201c', '"').replace('\u201d', '"')
    title = title.replace('\u2018', "'").replace('\u2019', "'")
    return title.strip().lower()


def add_page_to_module(token, course_id, module_id, page_url, position, indent=0):
    endpoint = f"{CANVAS_URL}/api/v1/courses/{course_id}/modules/{module_id}/items"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {
        "module_item": {
            "type": "Page",
            "page_url": page_url,
            "position": position,
            "indent": indent
        }
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code in [200, 201]:
        return True
    err = response.text.strip()[:200] if response.text else "no response body"
    print(f"    Warning: Failed to add page URL '{page_url}' (HTTP {response.status_code}): {err}")
    return False


def main():
    parser = argparse.ArgumentParser(description="Copy Canvas modules and page items between courses")
    parser.add_argument("--source", type=str, required=True, help="Source Canvas course ID (e.g. 63248)")
    parser.add_argument("--target", type=str, required=True, help="Target Canvas course ID (e.g. 65902)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    parser.add_argument("--rename-titles", action="store_true",
                        help="Rename existing target modules from Norwegian → English titles")
    args = parser.parse_args()

    token = get_api_token()
    source_id = args.source
    target_id = args.target

    print(f"\n{'='*70}")
    print(f"SYNC MODULES: {source_id} → {target_id}")
    if args.dry_run:
        print("*** DRY RUN — NO CHANGES WILL BE MADE ***")
    print(f"{'='*70}\n")

    # Load mapping files
    repo_root = Path(__file__).parent
    no_mapping = _load_mapping(repo_root / "page_id_mapping.json")
    en_mapping = _load_mapping(repo_root / "page_id_mapping.en.json")

    # Build lookups
    no_url_to_fp = {info['url']: fp for fp, info in no_mapping.items() if info.get('url')}
    en_fp_to_url = {fp: info['url'] for fp, info in en_mapping.items() if info.get('url')}

    # Fetch source modules
    endpoint = f"{CANVAS_URL}/api/v1/courses/{source_id}/modules?per_page=100"
    response = requests.get(endpoint, headers={"Authorization": f"Bearer {token}"})
    if response.status_code != 200:
        print(f"Error: Failed to fetch modules from course {source_id}")
        sys.exit(1)

    source_modules = sorted(response.json(), key=lambda m: m.get('position', 0))
    target_modules = get_modules(token, target_id)

    # Build module plan
    module_plan = []
    for mod in source_modules:
        pos = mod.get('position')
        src_name = mod.get('name', '')
        if not pos:
            continue
        tgt_name = MODULE_NAME_TRANSLATIONS.get(src_name, src_name)
        exists = pos in target_modules
        module_plan.append((pos, src_name, tgt_name, exists, mod['id']))

    # Print module preview
    print(f"{'Pos':<4} {'Source name':<45} {'Target name':<45} {'Status'}")
    print("-" * 105)
    for pos, src, tgt, exists, _ in module_plan:
        print(f"{pos:<4} {src:<45} {tgt:<45} {'EXISTS' if exists else 'CREATE'}")

    # Build item preview
    print("\nPage items to be placed:\n")
    print(f"{'Mod':<4} {'Page title':<45} {'Target URL (from mapping)'}")
    print("-" * 70)
    item_count = 0
    for pos, _, _, _, src_mod_id in module_plan:
        items = get_module_items(token, source_id, src_mod_id)
        for item in items:
            if item.get('type') != 'Page':
                continue
            no_url = item.get('page_url', '')
            fp = no_url_to_fp.get(no_url)
            en_url = en_fp_to_url.get(fp) if fp else None
            if en_url:
                print(f"{pos:<4} {item.get('title', ''):<45} {en_url}")
                item_count += 1
            else:
                print(f"{pos:<4} {item.get('title', ''):<45} (unmapped)")
    print(f"\nTotal page items: {item_count}")

    # Confirmation
    if args.dry_run:
        print("\n[DRY RUN] Nothing was changed.")
        return

    to_create = [m for m in module_plan if not m[3]]
    if not to_create and item_count == 0:
        print("\nNothing to do.")
        return

    if not args.yes:
        resp = input(f"\nCreate {len(to_create)} module(s) and add {item_count} page item(s)? [Y/n] ")
        if resp.strip().lower() not in ("", "y", "yes"):
            print("Cancelled.")
            return

    # Create missing modules
    for pos, _, tgt_name, exists, _ in module_plan:
        if exists:
            continue
        mid = create_module(token, target_id, tgt_name, pos)
        if mid:
            print(f"  ✓ Created module {pos}: {tgt_name} (ID {mid})")
            target_modules[pos] = mid
        else:
            print(f"  ✗ Failed to create module {pos}: {tgt_name}")

    # Refresh target modules
    target_modules = get_modules(token, target_id)

    # Rename existing modules that still have Norwegian titles
    if target_modules and args.rename_titles:
        print("\nChecking module titles...")
        target_names = get_module_names(token, target_id)
        renamed = 0
        for pos, module_id in target_modules.items():
            current_name = target_names.get(pos, '')
            new_name = MODULE_NAME_TRANSLATIONS.get(current_name)
            if new_name and current_name != new_name:
                if args.dry_run:
                    print(f"  [DRY RUN] Would rename: '{current_name}' → '{new_name}'")
                elif rename_module(token, target_id, module_id, new_name):
                    print(f"  ✓ Renamed: '{current_name}' → '{new_name}'")
                    renamed += 1
                else:
                    print(f"  ✗ Failed to rename module {pos}: '{current_name}'")
        if renamed == 0 and not args.dry_run:
            print("  No module titles needed renaming.")

    # Fetch all pages in the target course for title-based matching
    print(f"\nFetching all pages in target course {target_id}...")
    target_pages_by_title = fetch_target_pages(token, target_id)
    print(f"Found {len(target_pages_by_title)} page(s) in target course\n")

    # Add items — match English pages by title (robust against stale page_ids)
    added_total = 0
    skipped_total = 0
    for pos, _, tgt_name, _, src_mod_id in module_plan:
        if pos not in target_modules:
            continue
        tgt_mod_id = target_modules[pos]
        existing = get_existing_page_urls(token, target_id, tgt_mod_id)
        items = get_module_items(token, source_id, src_mod_id)

        added = 0
        skipped = 0
        for item in items:
            if item.get('type') != 'Page':
                continue
            no_url = item.get('page_url', '')
            fp = no_url_to_fp.get(no_url)
            if not fp:
                skipped += 1
                continue

            # Match by English title from the mapping file
            en_title = en_mapping.get(fp, {}).get('title', '')
            if not en_title:
                skipped += 1
                continue

            live_page = target_pages_by_title.get(_normalize_title(en_title))
            if not live_page:
                print(f"    ! No page titled '{en_title}' in course {target_id} (skipping)")
                skipped += 1
                continue

            live_url = live_page['url']
            if live_url in existing:
                continue  # already in this module

            ok = add_page_to_module(token, target_id, tgt_mod_id, live_url,
                                    item.get('position', 1), item.get('indent', 0))
            if ok:
                added += 1
            else:
                skipped += 1

        if added or skipped:
            print(f"  Module {pos} ({tgt_name}): added {added}, skipped {skipped}")
        added_total += added
        skipped_total += skipped

    print(f"\nDone. Added {added_total} item(s), skipped {skipped_total}.")


if __name__ == "__main__":
    main()
