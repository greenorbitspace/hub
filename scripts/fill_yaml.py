import os
from pathlib import Path

# Configure the root directory and supported file extensions
ROOT_DIR = Path("../userguide/content/en/docs/")  # current directory
EXTENSIONS = [".md"]

# Define your default YAML frontmatter
YAML_TEMPLATE = """---
title: "{title}"
description: ""
tags: []
draft: true
---
"""

def find_and_patch_empty_files(root_dir: Path):
    for path in root_dir.rglob("*"):
        if path.is_file() and path.suffix in EXTENSIONS:
            if path.stat().st_size == 0:
                title = path.stem.replace("-", " ").replace("_", " ").title()
                yaml_content = YAML_TEMPLATE.format(title=title)
                with path.open("w", encoding="utf-8") as f:
                    f.write(yaml_content)
                print(f"📝 Added YAML to: {path}")

if __name__ == "__main__":
    find_and_patch_empty_files(ROOT_DIR)