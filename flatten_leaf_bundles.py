import os
import shutil

BASE_DIR = "userguide/content/en/docs"
for root, dirs, files in os.walk(BASE_DIR):
    if 'index.md' in files:
        full_path = os.path.join(root, 'index.md')
        parent_dir = os.path.basename(root)
        new_name = os.path.join(os.path.dirname(root), parent_dir + '.md')

        print(f"Moving {full_path} → {new_name}")
        shutil.move(full_path, new_name)
        shutil.rmtree(root)