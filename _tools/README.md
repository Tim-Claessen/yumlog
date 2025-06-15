# 🛠️ Yumlog Developer Tools

This folder contains Python scripts used to manage and maintain the Yumlog cookbook. These scripts help automate common tasks and keep everything neat and organized.

These are currently required to be run manually, however in future should be further autoamted through GitHub Actions & Pull Requests.

## 📋 Overview of Scripts

### `form_to_md.py`

- Converts recipes from a Google Form (via linked Google Sheet) into Markdown files.
- Avoids duplicates based on timestamp.
- Saves new recipes into the `/recipes/` folder using the project’s recipe template.

### `update_indexes.py`

- Regenerates the index pages by:
  - Category
  - Protein
  - Alphabet
- Uses the recipe front matter to organise and update pages in `/indexes/`.

### `search_prep.py`

- Generates a `search.json` file used by the front-end to power the search bar on the site. It scans through the Markdown recipe files and extracts key fields like:
    - Title
    - Summary
    - Categories
    - Protein types
    - Cooking time

## 📦 Dependencies

Before running the scripts, ensure you have the required Python packages installed:

```bash
pip install -r requirements.txt
```