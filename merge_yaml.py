import os
import re
import yaml

def fix_ref_underscores(content):
    # Match YAML frontmatter block at the start of the file
    match = re.match(r'^(---\n.*?\n---)', content, re.DOTALL)
    if not match:
        return content  # no YAML frontmatter, return original content

    frontmatter = match.group(1)
    rest_of_file = content[len(frontmatter):]

    try:
        data = yaml.safe_load(frontmatter)
    except yaml.YAMLError:
        return content  # invalid YAML, skip file

    if not isinstance(data, dict):
        return content

    ref = data.get('ref')
    if isinstance(ref, str) and '_' in ref:
        fixed_ref = ref.replace('_', '-')
        data['ref'] = fixed_ref
        # Rebuild YAML frontmatter string
        new_frontmatter = "---\n" + yaml.dump(data, sort_keys=False, allow_unicode=True).strip() + "\n---"
        return new_frontmatter + rest_of_file
    else:
        return content

def process_md_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(subdir, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = fix_ref_underscores(content)
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated ref in: {path}")

def main():
    ROOT_DIR = "userguide/content/en/docs"  # Your base directory to process
    process_md_files(ROOT_DIR)
    print("Ref underscores replaced with hyphens in all Markdown files.")

if __name__ == "__main__":
    main()