import os
import re
import yaml
import unicodedata
import re

ROOT_DIR = "../userguide/content/en/docs"  # Adjust to your root docs folder

def slugify(value):
    """
    Convert folder name to a slug suitable for ref field:
    lowercase, spaces to hyphens, remove invalid chars.
    """
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value)
    return value

def read_front_matter(content):
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        body = fm_match.group(2)
        fm = yaml.safe_load(fm_text) or {}
        return fm, body
    else:
        # No front matter found
        return {}, content

def write_front_matter(fm, body):
    fm_yaml = yaml.dump(fm, sort_keys=False).strip()
    return f"---\n{fm_yaml}\n---\n{body}"

def update_index_titles_and_refs(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        if "_index.md" in filenames:
            index_path = os.path.join(dirpath, "_index.md")
            folder_name = os.path.basename(dirpath)
            slug = slugify(folder_name)

            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()

            fm, body = read_front_matter(content)

            updated = False
            if not fm.get("title") or fm["title"].strip() == "":
                fm["title"] = folder_name
                updated = True

            if not fm.get("ref") or fm["ref"].strip() == "":
                fm["ref"] = slug
                updated = True

            if updated:
                print(f"Updating _index.md at: {index_path}")
                new_content = write_front_matter(fm, body)
                with open(index_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

def main():
    update_index_titles_and_refs(ROOT_DIR)

if __name__ == "__main__":
    main()