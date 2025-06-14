import yaml
from pathlib import Path

CONTENT_DIR = Path("userguide/content/en/docs/notion-handbook")

def read_frontmatter(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != "---":
        return None, ''.join(lines)

    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            frontmatter = ''.join(lines[1:i])
            body = ''.join(lines[i+1:])
            try:
                data = yaml.safe_load(frontmatter) or {}
                return data, body
            except yaml.YAMLError:
                return None, ''.join(lines)
    return None, ''.join(lines)

def write_frontmatter(md_path, frontmatter, body):
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, sort_keys=False)
        f.write("---\n\n")
        f.write(body)

def sanitize_title(title):
    if not title:
        return None
    return str(title).strip()

def create_or_update_frontmatter(md_path):
    data, body = read_frontmatter(md_path)
    filename_title = md_path.stem.replace("-", " ").title()

    if data is None:
        # No or invalid frontmatter, create new
        data = {}

    # Ensure required fields
    if not data.get("title"):
        data["title"] = filename_title
    else:
        data["title"] = sanitize_title(data["title"])

    if not data.get("linkTitle"):
        data["linkTitle"] = data["title"]

    if "weight" not in data:
        data["weight"] = 10  # default weight

    if "draft" not in data:
        data["draft"] = False

    if "description" not in data:
        data["description"] = ""

    write_frontmatter(md_path, data, body)
    print(f"Processed: {md_path.name}")

def create_index_md():
    index_path = CONTENT_DIR / "_index.md"
    if index_path.exists():
        print(f"_index.md already exists, skipping.")
        return

    frontmatter = {
        "title": "Notion Handbook",
        "description": "Documentation and guides for Notion content",
        "weight": 20,
        "draft": False,
    }
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, sort_keys=False)
        f.write("---\n\n")
        f.write("")

    print("Created _index.md for notion-handbook section.")

def main():
    if not CONTENT_DIR.exists():
        print(f"Content directory does not exist: {CONTENT_DIR}")
        return

    md_files = list(CONTENT_DIR.glob("*.md"))

    for md_file in md_files:
        # Skip _index.md for now, handle separately
        if md_file.name == "_index.md":
            continue
        create_or_update_frontmatter(md_file)

    create_index_md()

if __name__ == "__main__":
    main()