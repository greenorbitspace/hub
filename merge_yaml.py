#!/usr/bin/env python3

import os
import re
import yaml
import unicodedata
import sys

ROOT_DIR = "userguide/content/en/docs"  # Update as needed

def slugify(value):
    """Generate a URL-friendly slug from a string"""
    value = str(value)
    value = unicodedata.normalize('NFKD', value)
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[\s_]+', '-', value).strip('-')

def format_title(title):
    """Format title by replacing underscores and capitalizing words"""
    return title.replace('_', ' ').strip().title()

def merge_yaml_blocks(content):
    blocks = re.findall(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
    body = re.split(r'^---\n.*?\n---\n', content, maxsplit=len(blocks), flags=re.DOTALL | re.MULTILINE)[-1]

    merged = {}
    for block in blocks:
        try:
            data = yaml.safe_load(block)
            if isinstance(data, dict):
                for key, value in data.items():
                    if key not in merged or not merged[key]:
                        merged[key] = value
            else:
                print("⚠️  Skipping non-dict YAML block")
        except yaml.YAMLError as e:
            print(f"❌ YAML parse error: {e}")
            continue

    # Title formatting and fallback logic
    if "title" in merged and merged["title"]:
        merged["title"] = format_title(merged["title"])
        merged["ref"] = merged.get("ref") or slugify(merged["title"])
    elif "ref" in merged and merged["ref"]:
        merged["title"] = merged.get("title") or merged["ref"].replace("-", " ").title()
    else:
        merged.setdefault("title", "Untitled")
        merged.setdefault("ref", "untitled")

    new_front_matter = yaml.dump(merged, sort_keys=False).strip()
    return f"---\n{new_front_matter}\n---\n{body.lstrip()}"

def process_md_files(path):
    for root, _, files in os.walk(path):
        for filename in files:
            if filename.endswith(".md"):
                full_path = os.path.join(root, filename)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    if content.count('---') >= 4:
                        print(f"🔄 Merging front matter in: {full_path}")
                        new_content = merge_yaml_blocks(content)

                        with open(full_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                    else:
                        print(f"✅ Skipping {full_path} — only one YAML block")
                except Exception as e:
                    print(f"❌ Failed to process {full_path}: {e}")

def main():
    if not os.path.exists(ROOT_DIR):
        print(f"❌ Directory not found: {ROOT_DIR}")
        sys.exit(1)

    print(f"📂 Scanning Markdown files in: {ROOT_DIR}")
    process_md_files(ROOT_DIR)
    print("✅ Merge complete.")

if __name__ == "__main__":
    main()