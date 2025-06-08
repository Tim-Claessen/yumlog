import os
import re
import json
import yaml

RECIPES_DIR = 'recipes'  # adjust if needed
OUTPUT_FILE = 'search.json'

def read_frontmatter_and_content(filepath):
  """
    Reads a Markdown file and extracts the YAML front matter and the content body.

    Args:
        filepath (str): Path to the Markdown (.md) file.

    Returns:
        tuple:
            - frontmatter (dict or None): Parsed YAML front matter as a dictionary. 
              Returns None if no front matter found.
            - content (str or None): The Markdown content excluding the front matter. 
              Returns None if no front matter found.
  """  
  with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Front matter is between --- lines at the top
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        return None, None

    fm_text, body = fm_match.groups()
    frontmatter = yaml.safe_load(fm_text)

    # Optionally, strip Markdown syntax for cleaner content here if needed
    # For now, keep raw Markdown body
    return frontmatter, body.strip()

def main():
    recipes = []

    for root, _, files in os.walk(RECIPES_DIR):
        for filename in files:
            if not filename.endswith('.md'):
                continue
            filepath = os.path.join(root, filename)
            fm, body = read_frontmatter_and_content(filepath)
            if fm and fm.get('layout') == 'recipe':
                recipes.append({
                    'title': fm.get('title', 'No Title'),
                    'url': fm.get('permalink') or f"/{os.path.relpath(filepath, RECIPES_DIR).replace('.md','/')}",
                    'content': body
                })

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(recipes, f, indent=2, ensure_ascii=False)

    print(f"Generated {OUTPUT_FILE} with {len(recipes)} recipes")

if __name__ == '__main__':
    main()