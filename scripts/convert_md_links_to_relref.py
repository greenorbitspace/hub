import re
from pathlib import Path

# Directory containing the markdown files
content_dir = Path("userguide/content/en/docs/notion-handbook")

# Regex to find the GitHub .md links you want to replace
pattern = re.compile(r'https://github\.com/google/docsy/tree/main/userguide/content/en/docs/notion-handbook/([a-z0-9\-]+)\.md')

for md_file in content_dir.rglob("*.md"):
    text = md_file.read_text(encoding="utf-8")
    new_text = pattern.sub(r'{{< ref "\1.md" >}}', text)
    if new_text != text:
        md_file.write_text(new_text, encoding="utf-8")
        print(f"Fixed links in: {md_file}")