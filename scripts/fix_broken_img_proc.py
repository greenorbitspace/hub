import os
import re
from pathlib import Path

# Configurable paths
CONTENT_DIR = Path("userguide/content")
ASSETS_IMAGES_DIR = Path("assets/images")
VALID_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}

# Regex to find imgproc shortcodes
IMGPROC_RE = re.compile(r"{{<\s*imgproc\s+([^>]+)\s*>}}")

# Regex to extract src attribute from shortcode
SRC_RE = re.compile(r'src\s*=\s*"([^"]+)"')

def find_imgproc_shortcodes(file_content):
    return IMGPROC_RE.findall(file_content)

def resolve_image_path(page_path, src):
    # Check relative to content file
    rel_path = (page_path.parent / src).resolve()
    if rel_path.exists():
        return rel_path

    # Check in assets/images
    asset_path = (ASSETS_IMAGES_DIR / src).resolve()
    if asset_path.exists():
        return asset_path

    return None

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = False
    matches = IMGPROC_RE.finditer(content)

    for match in reversed(list(matches)):
        shortcode = match.group(0)
        attrs = match.group(1)
        src_match = SRC_RE.search(attrs)

        if not src_match:
            print(f"❌ No src found in: {shortcode} in {file_path}")
            continue

        src = src_match.group(1)
        resolved = resolve_image_path(file_path, src)

        if not resolved:
            print(f"⚠️  Missing image: {src} → {file_path}")
            # Comment out the broken shortcode
            start, end = match.span()
            commented = f"<!-- BROKEN imgproc: {shortcode} -->"
            content = content[:start] + commented + content[end:]
            updated = True

    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated file: {file_path}")

def main():
    for md_file in CONTENT_DIR.rglob("*.md"):
        process_file(md_file)

if __name__ == "__main__":
    main()