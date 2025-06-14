import os

ROOT_DIR = "userguide/content/en/docs"  # Change this to your Hugo content root

FRONT_MATTER = """---
title: ""
description: ""
weight: 1
---"""

def ensure_index_file(folder_path):
    index_path = os.path.join(folder_path, "_index.md")
    if not os.path.exists(index_path):
        print(f"Creating missing _index.md in: {folder_path}")
        with open(index_path, "w") as f:
            f.write(FRONT_MATTER)

def main():
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        ensure_index_file(dirpath)

if __name__ == "__main__":
    main()