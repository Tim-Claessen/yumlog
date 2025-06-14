"""
update_indexes.py
-----------------
Script to update website index pages for recipes by Category, Protein, and Alphabet.

It reads Markdown recipe files from the `recipes/` folder,
extracts front matter metadata,
and generates or updates index markdown files under `indexes/category/`, `indexes/protein/`, and `indexes/alphabet.md`.

Handles existing content preservation and logs progress and errors.
"""

#Libraries
import os
import re
import yaml
import sys
from collections import defaultdict

# Constants - change these as needed or pass as args
RECIPE_DIR = "recipes"
INDEX_DIR = "indexes"
PLACEHOLDER_TEXT_START = "⏳ This page is still simmering 🍳"
OUTPUT_DIRS = {
    "category": "category",
    "protein": "protein"
}

# ------------------------------------------------------------------------------

def extract_yaml_front_matter(filepath):
    """
    Extract YAML front matter from a Markdown file.

    Args:
        filepath (str): Path to the markdown file.

    Returns:
        dict: Parsed YAML front matter or None if not found/invalid.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if not lines or lines[0].strip() != "---":
            return None
        yaml_lines = []
        for line in lines[1:]:
            if line.strip() == "---":
                break
            yaml_lines.append(line)
        return yaml.safe_load("".join(yaml_lines))
    except Exception as e:
        print(f"❌ Error reading YAML front matter from {filepath}: {e}")
        return None

def normalize_value(value):
    """
    Normalize a string by removing wikilink brackets [[ and ]], and trimming whitespace.

    Args:
        value (str): Raw string from front matter.

    Returns:
        str: Normalized string.
    """
    if not isinstance(value, str):
        return ""
    return re.sub(r"\[\[(.*?)\]\]", r"\1", value).strip().lower()

def get_field_values(field_data):
    """
    Handle field data which can be string or list of strings, normalize all values.

    Args:
        field_data (str or list): Raw field data from YAML.

    Returns:
        list of str: List of normalized values.
    """
    if isinstance(field_data, list):
        return [normalize_value(item) for item in field_data if item]
    elif isinstance(field_data, str):
        # Single string - normalize and return as single item list
        return [normalize_value(field_data)]
    return []

def format_link(title, filename):
    """
    Format a markdown link list item to a recipe.

    Args:
        title (str): Recipe title.
        filename (str): Recipe markdown filename.

    Returns:
        str: Markdown formatted link list item.
    """
    return f"- [{title}](../{RECIPE_DIR}/{filename})"

def load_existing_file(filepath):
    """
    Load existing output file lines excluding placeholder block if present.

    Args:
        filepath (str): Path to output file.

    Returns:
        list of str: Lines before first list item or placeholder.
    """
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        if PLACEHOLDER_TEXT_START in line:
            # Stop on placeholder start (remove whole block)
            break
        if line.strip().startswith("- "):
            # Stop before list items
            break
        cleaned_lines.append(line)
    return cleaned_lines

def update_index_pages(field_name):
    """
    Read all recipes and update index pages based on the given field.

    Args:
        field_name (str): Front matter field to index by (e.g., "category", "protein").
    """
    output_dir = OUTPUT_DIRS.get(field_name)
    if not output_dir:
        print(f"❌ No output directory configured for field '{field_name}'")
        return

    os.makedirs(output_dir, exist_ok=True)

    index_map = defaultdict(list)  # map normalized value -> list of (title, filename)

    for filename in os.listdir(RECIPE_DIR):
        if not filename.endswith(".md"):
            continue

        path = os.path.join(RECIPE_DIR, filename)
        front = extract_yaml_front_matter(path)
        if not front:
            print(f"⚠️ Skipping {filename}: no or invalid front matter")
            continue

        field_data = front.get(field_name)
        if not field_data:
            print(f"⚠️ Skipping {filename}: missing '{field_name}' field")
            continue

        titles = front.get("title") or filename.replace("_", " ").replace(".md", "")
        values = get_field_values(field_data)

        if not values:
            print(f"⚠️ Skipping {filename}: no valid {field_name} values found")
            continue

        for value in values:
            index_map[value].append((titles, filename))

    # Write index files
    for value, recipes in index_map.items():
        output_filename = f"{value.lower().replace(' ', '_')}.md"
        output_path = os.path.join(output_dir, output_filename)

        # Load existing heading or start fresh
        existing_header = load_existing_file(output_path)
        if not existing_header:
            # Create default heading
            header_line = f"# {value.title()}\n\n"
            existing_header = [header_line]

        # Sort recipes by title
        recipes.sort(key=lambda x: x[0].lower())

        # Format links
        link_lines = [format_link(title, fname) for title, fname in recipes]

        # Write output file
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.writelines(existing_header)
                f.write("\n".join(link_lines) + "\n")
            print(f"✅ Updated {field_name} page: {output_filename} ({len(recipes)} recipes)")
        except Exception as e:
            print(f"❌ Failed to write {output_path}: {e}")

def update_alphabet_index(recipe_dir, index_dir):
    """
    Generate or update an alphabetical index markdown file listing all recipes.

    This function scans all Markdown recipe files in `recipe_dir`, extracts their titles
    (from YAML front matter if available, else from filename), sorts them alphabetically,
    and writes a Markdown index file at `index_dir/alphabet.md`.

    Existing file header/frontmatter before the recipe list is preserved.
    Any placeholder block starting with PLACEHOLDER_TEXT_START is removed.

    Args:
        recipe_dir (str): Directory containing recipe markdown files.
        index_dir (str): Directory where the alphabetical index file will be written.
    """
    output_path = os.path.join(index_dir, "alphabet.md")

    recipes = []
    for filename in os.listdir(recipe_dir):
        if not filename.endswith('.md'):
            continue
        path = os.path.join(recipe_dir, filename)
        try:
            front = extract_yaml_front_matter(path)
            if front and 'title' in front and isinstance(front['title'], str):
                title = front['title']
            else:
                title = filename.replace("_", " ").replace(".md", "")
            recipes.append((title, filename))
        except Exception as e:
            print(f"⚠️ Skipping {filename} for alphabetical index due to error: {e}")

    recipes.sort(key=lambda x: x[0].lower())

    # Load existing header lines if file exists, else default header
    before_links = []
    if os.path.exists(output_path):
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_lines = f.readlines()
        except Exception as e:
            print(f"❌ Failed to read existing alphabet index file: {e}")
            existing_lines = []

        for line in existing_lines:
            if PLACEHOLDER_TEXT_START in line:
                # Stop and remove placeholder block if found
                print(f"🧹 Removed placeholder block from alphabetical index")
                break
            if line.strip().startswith("- "):
                # Stop before list items start
                break
            before_links.append(line)
    else:
        before_links = ["# 🔤 Alphabetical Index\n\n"]

    link_lines = [f"- [{title}](../{RECIPE_DIR}/{fname})" for title, fname in recipes]

    os.makedirs(index_dir, exist_ok=True)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(before_links)
            f.write("\n".join(link_lines) + "\n")
        print(f"🎉 All done updating alphabet index page.")
    except Exception as e:
        print(f"❌ Failed to write alphabetical index file: {e}")


if __name__ == "__main__":
    try:
        for field in ["category", "protein"]:
                update_index_pages(field)
                print(f"🎉 All done updating {field} pages.")
        
        update_alphabet_index(RECIPE_DIR, INDEX_DIR)
        print("✅ All indexes updated successfully.")
        
    except Exception as e:
        print(f"❌ Script failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
