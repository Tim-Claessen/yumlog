"""
search_prep.py
---------------------
Script to generate the `search.json` file for client-side website search.

It scans the `recipes/` folder for Markdown recipe files,
extracts YAML front matter and cleans Markdown content,
then compiles searchable data (title, URL, content) into a JSON index.

Handles missing dependencies gracefully and outputs the final index as `search.json`.
"""

#Libraries
import os
import re
import json
try:
    import yaml
except ImportError:
    print("Missing dependency 'pyyaml'. Please run: pip install pyyaml")
    exit(1)

#Define variables
RECIPES_DIR = 'recipes'
OUTPUT_FILE = 'search.json'

# ------------------------------------------------------------------------------

def read_frontmatter_and_content(filepath):
    """
    Reads a Markdown file and extracts the YAML front matter and content body.

    Args:
        filepath (str): Path to the Markdown (.md) file.

    Returns:
        tuple:
            - frontmatter (dict or None): Parsed front matter dict, or None if absent.
            - content (str or None): Body text with Markdown stripped, or None if no front matter.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match YAML front matter at the top of the file
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        return None, None

    fm_text, body = fm_match.groups()
    frontmatter = yaml.safe_load(fm_text)
    stripped_body = strip_markdown(body)

    return frontmatter, stripped_body

def strip_markdown(text):
    """
    Naively strips common Markdown syntax from text for cleaner search indexing.

    Args:
        text (str): Markdown content.

    Returns:
        str: Plain text with basic Markdown stripped.
    """
    text = re.sub(r'`{1,3}(.*?)`{1,3}', r'\1', text)            # inline/backtick code
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)                 # images
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)        # links
    text = re.sub(r'[*_]{1,3}(.*?)[*_]{1,3}', r'\1', text)       # bold/italic
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)      # headings
    text = re.sub(r'^[-*+]\s+', '', text, flags=re.MULTILINE)   # bullet points
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)   # numbered lists
    text = re.sub(r'>\s?', '', text)                            # blockquotes
    text = re.sub(r'\n{2,}', '\n', text)                        # collapse multiple newlines
    return text.strip()

def main():
    """
    Walks through the recipe directory and extracts searchable recipe info into a JSON file.
    """
    recipes = []

    for root, _, files in os.walk(RECIPES_DIR):
        for filename in files:
            if not filename.lower().endswith('.md'):
                continue

            filepath = os.path.join(root, filename)
            fm, body = read_frontmatter_and_content(filepath)

            if fm and fm.get('layout') == 'recipe':
                recipes.append({
                    'title': fm.get('title', 'No Title'),
                    'url': fm.get('permalink') or f"/yumlog/recipes/{os.path.relpath(filepath, RECIPES_DIR).replace('.md','.html')}",
                    'content': body
                })

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(recipes, f, indent=2, ensure_ascii=False)

    print(f"Generated {OUTPUT_FILE} with {len(recipes)} recipes")

if __name__ == '__main__':
    main()