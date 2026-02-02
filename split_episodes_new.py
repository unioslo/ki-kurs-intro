#!/usr/bin/env python3
"""
Split episode files into smaller parts:
- episode_0.rst: Oversikt, Temaer som dekkes, Læringsmål
- episode_1.rst, episode_2.rst, etc.: Each main section (marked by ~~~)
"""

import re
import os


def split_episode(filepath):
    """Split an episode file into smaller parts."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get episode number from filename (e.g., episode3.rst -> 3)
    episode_num = re.search(r'episode(\d+)\.rst', filepath).group(1)
    base_dir = os.path.dirname(filepath)

    lines = content.split('\n')

    # Find the main title (first line with ====== underline)
    main_title = None
    main_title_idx = -1
    for i, line in enumerate(lines):
        if '===' in line and i > 0:
            main_title = lines[i-1]
            main_title_idx = i - 1
            break

    if not main_title:
        print(f"Could not find main title in {filepath}")
        return

    # Find where "Oversikt" section ends
    # Look for the first section after "Oversikt" that has ~~~ underline
    # and is NOT "Temaer som dekkes" or "Læringsmål"
    overview_end_idx = len(lines)
    in_overview = False

    for i, line in enumerate(lines):
        # Skip the main title
        if i <= main_title_idx + 1:
            continue

        # Check for "Oversikt" section
        if 'Oversikt' in line and i + 1 < len(lines) and '---' in lines[i + 1]:
            in_overview = True
            continue

        # If we're past Oversikt and find a ~~~ underline
        if in_overview and i + 1 < len(lines) and lines[i + 1].strip():
            if all(c == '~' for c in lines[i + 1].strip()):
                # Check if this is NOT a subsection of Oversikt
                if 'Temaer som dekkes' not in line and 'Læringsmål' not in line:
                    overview_end_idx = i
                    break

    # Create episode_0.rst with overview
    overview_content = '\n'.join(lines[:overview_end_idx]).rstrip() + '\n'
    overview_file = os.path.join(base_dir, f'episode{episode_num}_0.rst')
    with open(overview_file, 'w', encoding='utf-8') as f:
        f.write(overview_content)
    print(f"Created: {overview_file}")

    # Now split remaining content by main sections (those with ~~~ underline)
    sections = []
    current_section = []
    skip_next = False

    for i in range(overview_end_idx, len(lines)):
        if skip_next:
            skip_next = False
            continue

        line = lines[i]

        # Check if next line is ~~~ underline
        if i + 1 < len(lines) and lines[i + 1].strip() and all(c == '~' for c in lines[i + 1].strip()):
            # Start of a new section
            if current_section:
                sections.append('\n'.join(current_section))
            current_section = [main_title, '=' * len(main_title), '', line, lines[i + 1]]
            skip_next = True  # Skip the underline on next iteration
        elif current_section:
            current_section.append(line)

    # Add last section
    if current_section:
        sections.append('\n'.join(current_section))

    # Write each section to its own file
    for idx, section_content in enumerate(sections, start=1):
        section_file = os.path.join(base_dir, f'episode{episode_num}_{idx}.rst')
        with open(section_file, 'w', encoding='utf-8') as f:
            f.write(section_content.rstrip() + '\n')
        print(f"Created: {section_file}")

    print(f"Split {filepath} into {len(sections) + 1} files\n")


def main():
    """Split all episode files."""
    episode_files = [
        'source/episodes/episode1.rst',
        'source/episodes/episode2.rst',
        'source/episodes/episode3.rst',
        'source/episodes/episode4.rst',
        'source/episodes/episode5.rst',
        'source/episodes/episode6.rst',
    ]

    for filepath in episode_files:
        if os.path.exists(filepath):
            split_episode(filepath)
        else:
            print(f"File not found: {filepath}")


if __name__ == '__main__':
    main()
