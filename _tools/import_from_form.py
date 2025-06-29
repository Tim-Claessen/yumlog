"""
import_from_form.py
------------------
Script to import new recipe submissions from a Google Sheet (via Google Forms),
convert each into a Markdown file based on a template,
and save them into the `recipes/` folder.

It tracks the processing in the Google Sheet
and is designed for local runs or GitHub Actions compatibility.
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pytz

# CONFIGURATION

# Google service account JSON key (loaded from GitHub Actions secret or environment)
SERVICE_ACCOUNT_JSON = os.environ.get('GOOGLE_SERVICE_ACCOUNT_JSON')

# Google Sheet and Worksheet names
SHEET_NAME = "Yumlog-RecipeUpload"
WORKSHEET_NAME = "FormResponses1"

# Paths inside repo
REPO_ROOT = Path(__file__).parent.parent
RECIPES_DIR = REPO_ROOT / 'recipes'
DATA_DIR = REPO_ROOT / '_data'

# Timezone for timestamps
LOCAL_TZ = pytz.timezone('Australia/Perth')  # GMT+8

# Essential fields to check before processing a recipe
ESSENTIAL_FIELDS = ['Recipe Title', 'Ingredients', 'Instructions', 'Category', 'Protein']

# ------------------------------------------------------------------------------

def snake_case_filename(title: str) -> str: 
    """
    Convert a recipe title into a snake_case filename.
    Removes non-alphanumeric characters except spaces, then replaces spaces with underscores.
    """
    title_clean = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    title_snake = re.sub(r'\s+', '_', title_clean.strip().lower())
    return f"{title_snake}.md"

def parse_tags(tags_field: str) -> list[str]:
    """
    Parse tags field from form, expecting something like '#tag1 #tag2'
    Returns a list of lowercase tags without '#'.
    """
    if not tags_field:
        return []
    tags = re.findall(r'#(\w+)', tags_field)
    return [tag.lower() for tag in tags]

def parse_list_field(field: str) -> list[str]: 
    """
    Parse multi-item fields that are newline-separated.
    Returns list of stripped strings.
    """
    if not field:
        return []
    # Split only by newlines
    items = field.split('\n')
    return [item.strip() for item in items if item.strip()]

def format_markdown(recipe: dict) -> str: 
    """
    Format the recipe dictionary into markdown text with frontmatter.
    Expected keys:
     - title, category, protein (list), prep_time_mins, total_time_mins, source,
       tags (list), date_created (YYYY-MM-DD), ingredients (list), instructions (list)
    """
    # Frontmatter
    frontmatter_lines = [
        '---',
        f"title: {recipe['title']}",
        f"category: \"[[{recipe['category']}]]\"" if recipe.get('category') else "category: \"\"",
        "protein:",
    ]
    if recipe.get('protein'):
        for p in recipe['protein']:
            frontmatter_lines.append(f"  - \"[[{p}]]\"")
    else:
        frontmatter_lines.append("  - \"\"")
    frontmatter_lines.extend([
        f"prep_time_mins: {recipe.get('prep_time_mins', '')}",
        f"total_time_mins: {recipe.get('total_time_mins', '')}",
        f"source: {recipe.get('source', '')}",
        "tags:",
    ])
    if recipe.get('tags'):
        for t in recipe['tags']:
            frontmatter_lines.append(f"  - {t}")
    else:
        frontmatter_lines.append("  - ")
    frontmatter_lines.append(f"date_created: {recipe.get('date_created', '')}")
    frontmatter_lines.append("layout: recipe")
    frontmatter_lines.append('---\n')

    # Body markdown
    body_lines = [
        f"# {recipe['title']}\n",
        "## Ingredients\n",
    ]
    for ingredient in recipe.get('ingredients', []):
        body_lines.append(f"{ingredient}")
    body_lines.append("\n## Instructions\n")
    for instruction in recipe.get('instructions', []):
        body_lines.append(f"{instruction}")

    return '\n'.join(frontmatter_lines + body_lines)

def convert_timestamp_to_local(dt_str: str) -> datetime: 
    """
    Convert timestamp string from Google Sheets (e.g. "6/14/2025 11:13:54") to localized datetime.
    Assumes input is in local time GMT+8.
    """
    dt_naive = datetime.strptime(dt_str, '%m/%d/%Y %H:%M:%S')
    dt_local = LOCAL_TZ.localize(dt_naive)
    return dt_local

def main():
    print("Starting recipe import from Google Sheet")

    updates = []

    # Authenticate and open Google Sheet
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    if SERVICE_ACCOUNT_JSON:
        # GitHub Actions: parse JSON from environment variable
        creds_dict = json.loads(SERVICE_ACCOUNT_JSON)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    else:
        # Local run fallback: load from file
        SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '..', '_secrets', 'google_service_account.json')
        creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)

    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME)
    worksheet = sheet.worksheet(WORKSHEET_NAME)

    rows = worksheet.get_all_records()
    print(f"Total rows fetched: {len(rows)}")
    headers = worksheet.row_values(1)
   
   #Grab 'processed' column to track changes
    if 'Processed' not in headers:
        worksheet.update_cell(1, len(headers) + 1, 'Processed')
        headers.append('Processed')   
    processed_col_index = headers.index('Processed') + 1

    processed_count = 0
    skipped_count = 0

    for idx, row in enumerate(rows, 1):
        try:
            # Skip if already processed
            processed_raw = row.get('Processed')

            if processed_raw == 'Yes':
                skipped_count += 1
                updates.append({'range': f"{gspread.utils.rowcol_to_a1(idx + 1, processed_col_index)}", 'values': [['Yes']]})
                continue

            if processed_raw == 'Skipped':
                skipped_count += 1
                updates.append({'range': f"{gspread.utils.rowcol_to_a1(idx + 1, processed_col_index)}", 'values': [['Skipped']]})
                continue

            # Check essential fields
            missing_essentials = [field for field in ESSENTIAL_FIELDS if not row.get(field)]
            if missing_essentials:
                print(f"Row {idx} skipped: missing essential fields {missing_essentials}")
                skipped_count += 1
                updates.append({'range': f"{gspread.utils.rowcol_to_a1(idx + 1, processed_col_index)}", 'values': [['Skipped']]})
                continue

            # Prepare recipe dict from row
            recipe = {
                'title': row['Recipe Title'].strip(),
                'category': row.get('Category', '').strip().lower().replace(" & ", "_"),
                'protein': [p.lower().replace(' & ', '_') for p in parse_list_field(row.get('Protein', ''))],
                'prep_time_mins': int(row.get('Prep Time (in minutes)', 0) or 0),
                'total_time_mins': int(row.get('Total Time (in minutes)', 0) or 0),
                'source': row.get('Source of recipe', '').strip(),
                'tags': parse_tags(row.get('Tags', '')),
                'date_created': datetime.now(LOCAL_TZ).strftime('%Y-%m-%d'),
                'ingredients': [line.strip() for line in row.get('Ingredients', '').splitlines() if line.strip()],
                'instructions': [line.strip() for line in row.get('Instructions', '').splitlines() if line.strip()],
            }

            # Generate filename
            filename = snake_case_filename(recipe['title'])
            filepath = RECIPES_DIR / filename

            if filepath.exists():
                print(f"Warning: '{filename}' already exists. Skipping to avoid overwrite.")
                skipped_count += 1
                updates.append({'range': f"{gspread.utils.rowcol_to_a1(idx + 1, processed_col_index)}", 'values': [['Skipped']]})
                continue

            # Save markdown file
            RECIPES_DIR.mkdir(parents=True, exist_ok=True)
            md_content = format_markdown(recipe)
            with open(filepath, 'w', encoding='utf-8') as f_md:
                f_md.write(md_content)

            print(f"Row {idx} processed: saved '{filename}'")
            processed_count += 1

            # Mark record as 'Processed'
            updates.append({'range': f"{gspread.utils.rowcol_to_a1(idx + 1, processed_col_index)}", 'values': [['Yes']]})

        except Exception as e:
            print(f"Row {idx} error: {e}")
            updates.append({'range': f"{gspread.utils.rowcol_to_a1(idx + 1, processed_col_index)}", 'values': [['Skipped']]})
            skipped_count += 1
            continue
    
    if updates:
        worksheet.batch_update(updates)
    print(f"Import completed: {processed_count} recipes processed, {skipped_count} skipped. Ensure the index pages and search are updated if new recipes were added.")

if __name__ == "__main__":
    main()
