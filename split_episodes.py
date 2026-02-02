#!/usr/bin/env python3
"""
Split episode RST files into smaller files for Canvas integration.
Each episode gets:
- episodeN_overview.rst (Oversikt, Temaer som dekkes, Læringsmål)
- episodeN_1.rst, episodeN_2.rst, etc. (one per main section)
"""

import re
import os

def split_episode(episode_num, input_file, output_dir):
    """Split an episode file into multiple smaller files."""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by sections (marked by ~~~ underlines)
    # Pattern: capture section title and its content until next section
    lines = content.split('\n')

    sections = []
    current_section = []
    section_title = None
    in_section = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check if next line is a section marker (~~~)
        if i + 1 < len(lines) and re.match(r'^~+$', lines[i + 1]):
            # Save previous section
            if current_section:
                sections.append({
                    'title': section_title,
                    'content': '\n'.join(current_section)
                })

            # Start new section
            section_title = line
            current_section = []
            in_section = True
            i += 2  # Skip title and ~~~ line
            continue

        if in_section:
            current_section.append(line)

        i += 1

    # Add last section
    if current_section:
        sections.append({
            'title': section_title,
            'content': '\n'.join(current_section)
        })

    # Extract episode title and intro
    first_lines = []
    for line in lines:
        if re.match(r'^=+$', line):
            break
        first_lines.append(line)

    # Find episode title (line before ===)
    episode_title = None
    for i, line in enumerate(lines):
        if re.match(r'^=+$', line) and i > 0:
            episode_title = lines[i-1]
            break

    # Create overview file
    overview_content = f"""{episode_title}
{"=" * len(episode_title)}

.. contents::
   :local:
   :depth: 2

"""

    # Add first few sections to overview (Oversikt, Temaer, Læringsmål)
    for i, section in enumerate(sections[:3]):
        if section['title']:
            overview_content += f"{section['title']}\n"
            overview_content += "~" * len(section['title']) + "\n\n"
            overview_content += section['content'].strip() + "\n\n"

    # Write overview file
    overview_file = os.path.join(output_dir, f'episode{episode_num}_overview.rst')
    with open(overview_file, 'w', encoding='utf-8') as f:
        f.write(overview_content)
    print(f"Created: {overview_file}")

    # Create individual section files (skip first 3: Oversikt, Temaer, Læringsmål)
    section_num = 1
    for section in sections[3:]:
        if not section['title']:
            continue

        section_content = f"""{episode_title}
{"=" * len(episode_title)}

{section['title']}
{"~" * len(section['title'])}

{section['content'].strip()}
"""

        section_file = os.path.join(output_dir, f'episode{episode_num}_{section_num}.rst')
        with open(section_file, 'w', encoding='utf-8') as f:
            f.write(section_content)
        print(f"Created: {section_file}")
        section_num += 1

    return section_num - 1  # Return number of sections created


# Main execution
if __name__ == '__main__':
    source_dir = 'source/episodes'
    output_dir = 'source/episodes'

    # Process each episode
    for ep_num in range(1, 7):
        input_file = os.path.join(source_dir, f'episode{ep_num}.rst')
        if os.path.exists(input_file):
            print(f"\n=== Processing Episode {ep_num} ===")
            num_sections = split_episode(ep_num, input_file, output_dir)
            print(f"Episode {ep_num}: Created overview + {num_sections} section files")
