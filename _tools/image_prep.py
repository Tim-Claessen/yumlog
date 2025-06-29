"""
image_convert.py
---------------------
Script to convert, compress, and optionally resize images in bulk.

Scans the `images/raw/` directory for supported image formats,
converts them to the specified output format, resizes them while preserving
aspect ratio, and compresses based on the selected quality setting.

Outputs all processed images to the `iamges/` folder.
"""

# Libraries
import os
try:
    from PIL import Image
except ImportError:
    print("Missing dependency 'Pillow'. Please run: pip install pillow")
    exit(1)

# Define variables
INPUT_DIR = 'images/raw/'
OUTPUT_DIR = 'images/'
OUTPUT_FORMAT = 'WEBP'       # Options: JPEG, PNG, WEBP, etc.
RESIZE_TO = None      # (width, height) or None to skip resizing
QUALITY = 75                 # JPEG/WEBP quality (0–100)
SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff')

# ------------------------------------------------------------------------------

def convert_image(input_path, output_path, resize_to=None, output_format='JPEG', quality=85):
    """
    Converts, compresses, and optionally resizes a single image.

    Args:
        input_path (str): Path to the source image file.
        output_path (str): Path where the output image will be saved.
        resize_to (tuple or None): Resize target as (width, height), or None to skip.
        output_format (str): Output image format (e.g. 'JPEG', 'PNG').
        quality (int): Compression quality (0–100).
    """
    with Image.open(input_path) as img:
        if output_format.upper() == 'JPEG' and img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        if resize_to:
            img.thumbnail(resize_to)  # Preserves aspect ratio

        img.save(output_path, output_format, quality=quality)


def main():
    """
    Walks through input directory and processes all supported images.
    Saves output images in the specified format and quality.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(SUPPORTED_EXTENSIONS):
            continue

        input_path = os.path.join(INPUT_DIR, filename)
        base_name = os.path.splitext(filename)[0]
        output_ext = OUTPUT_FORMAT.lower()
        output_path = os.path.join(OUTPUT_DIR, f"{base_name}.{output_ext}")

        #check if file already exists
        if os.path.exists(output_path):
            print(f"Skipped: {output_path} already exists.")
            continue

        convert_image(input_path, output_path, RESIZE_TO, OUTPUT_FORMAT, QUALITY)
        count += 1
        print(f"Processed: {output_path}")

    print(f"✅ Completed: {count} image(s) converted to {OUTPUT_FORMAT} in '{OUTPUT_DIR}'. \nClean up any files from '{INPUT_DIR}'.")


if __name__ == '__main__':
    main()