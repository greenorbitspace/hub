import re
from pathlib import Path

CONTENT_DIR = Path("userguide/content/en/docs/notion-handbook")

# Regex to find markdown links: [text](url)
LINK_REGEX = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)\)', re.IGNORECASE)

# Detect GitHub absolute URLs (change this to match your repo URL pattern)
GITHUB_URL_PREFIX = "https://github.com/google/docsy/tree/main/userguide/content/en/docs/notion-handbook/"

def convert_link_url(url: str) -> str:
    # If URL starts with GitHub raw or tree URL, convert to relative path
    if url.startswith(GITHUB_URL_PREFIX):
        relative_path = url[len(GITHUB_URL_PREFIX):]
        # Ensure relative_path does not start with '/' or '.'
        relative_path = relative_path.lstrip("/.")

        # Return Hugo relref shortcode
        return '{{< relref "notion-handbook/' + relative_path + '" >}}'
    # If already relative or other links, return as is
    return url

def process_file(filepath: Path):
    content = filepath.read_text(encoding="utf-8")
    changed = False

    def replace_link(match):
        nonlocal changed
        text, url = match.groups()
        new_url = convert_link_url(url)
        if new_url != url:
            changed = True
            return f'[{text}]({new_url})'
        return match.group(0)

    new_content = LINK_REGEX.sub(replace_link, content)

    if changed:
        filepath.write_text(new_content, encoding="utf-8")
        print(f"Updated links in: {filepath}")

def main():
    md_files = CONTENT_DIR.rglob("*.md")
    for md_file in md_files:
        process_file(md_file)

if __name__ == "__main__":
    main()