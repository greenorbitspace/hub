import os
import re
import yaml

# Path to the directory you'd like to process (recursively)
ROOT_DIR = "userguide/content/en/docs/"  # Change to "userguide/content/en/docs" or any target dir

def merge_yaml_blocks(content):
    yaml_blocks = list(re.finditer(r"^---\n(.*?)\n---", content, flags=re.DOTALL | re.MULTILINE))
    
    if not yaml_blocks:
        return content  # No YAML front matter found

    # Extract YAML content and merge
    merged_data = {}
    for block in yaml_blocks:
        data = yaml.safe_load(block.group(1))
        if isinstance(data, dict):
            for key, value in data.items():
                if key not in merged_data or merged_data[key] in ("", None):
                    merged_data[key] = value

    # Clean title
    if "title" in merged_data:
        cleaned = merged_data["title"].replace("_", " ").replace("-", " ").strip().title()
        merged_data["title"] = cleaned

    # Clean ref (kebab-case)
    if "ref" in merged_data:
        merged_data["ref"] = merged_data["ref"].replace("_", "-")

    # Rebuild YAML and content
    new_yaml = f"---\n{yaml.dump(merged_data, sort_keys=False).strip()}\n---"
    last_block = yaml_blocks[-1]
    remaining_content = content[last_block.end():].lstrip()
    
    return f"{new_yaml}\n\n{remaining_content}"

def process_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    original = f.read()

                updated = merge_yaml_blocks(original)

                if original != updated:
                    print(f"✅ Fixed: {path}")
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(updated)
                else:
                    print(f"👌 No changes: {path}")

if __name__ == "__main__":
    process_files(ROOT_DIR)