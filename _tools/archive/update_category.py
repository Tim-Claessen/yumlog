# Libraries
import os
import yaml
from collections import defaultdict

# Directory paths
RECIPE_DIR = "recipes"
CATEGORY_DIR = "category"

def extract_yaml_front_matter(filepath):
    """
    Extract the YAML front matter from a Markdown file.

    Args:
        filepath (str): Path to the Markdown file.

    Returns:
        dict or None: Parsed YAML front matter as a dictionary, or None if invalid.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != "---":
        return None  # No YAML front matter

    yaml_lines = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        yaml_lines.append(line)

    try:
        return yaml.safe_load("".join(yaml_lines))
    except yaml.YAMLError as e:
        print(f"YAML error in {filepath}: {e}")
        return None

def format_link(title, filename):
    """
    Create a Markdown link to a recipe.

    Args:
        title (str): Recipe title.
        filename (str): Filename of the recipe.

    Returns:
        str: Markdown-formatted list item with link to recipe.
    """
    rel_path = f"../{RECIPE_DIR}/{filename}"
    return f"- [{title}]({rel_path})"

def main():
    """
    Scan all recipe Markdown files, group them by category,
    and update corresponding category index files in the category folder.
    """
    # Map from category name → list of formatted Markdown links
    category_recipes = defaultdict(list)

    # Loop through each recipe file
    for filename in os.listdir(RECIPE_DIR):
        if not filename.endswith(".md"):
            continue  # Skip non-markdown files

        path = os.path.join(RECIPE_DIR, filename)
        front = extract_yaml_front_matter(path)
        if not front:
            continue  # Skip if front matter couldn't be parsed

        category = front.get("category", "").strip()
        title = front.get("title", filename.replace("_", " ").replace(".md", ""))

        # Skip invalid or empty categories
        if not category.startswith("[[") or not category.endswith("]]"):
            continue

        # Normalize category name by removing [[ and ]]
        category_name = category[2:-2]

        # Add formatted link to this category
        category_recipes[category_name].append(format_link(title, filename))

    # Generate or update a file for each category
    for category_name, links in category_recipes.items():
        links.sort()  # Sort recipe list alphabetically

        output_filename = f"{category_name.lower().replace(' ', '_')}.md"
        output_path = os.path.join(CATEGORY_DIR, output_filename)

        # Default heading (preserve custom ones if file exists)
        heading = f"# {category_name.title()}"

        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                existing_lines = f.readlines()

            # Remove placeholder block if present
            placeholder_start = "⏳ This page is still simmering 🍳"
            placeholder_found = False
            before_links = []
            for line in existing_lines:
                if placeholder_start in line:
                    placeholder_found = True
                    break
                if line.strip().startswith("- "):
                    break
                before_links.append(line)

            if placeholder_found:
                print(f"🧹 Removed placeholder from: {category_name}")

        except FileNotFoundError:
            # Start fresh if file doesn't exist
            before_links = [heading + "\n\n"]

        # Write updated category file
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.writelines(before_links)
                f.write("\n".join(links) + "\n")
        except Exception as e:
            print(f"❌ Failed to write to {output_path}: {e}")

        print(f"✅ Updated: {category_name} ({len(links)} recipes)")
        
    print("✅ Category pages updated successfully.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Script failed with error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)