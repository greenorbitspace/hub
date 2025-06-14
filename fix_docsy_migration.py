import os
from pathlib import Path

THEME_LAYOUTS_DIR = Path('layouts/_default')

def rename_taxonomy_files():
    taxonomy = THEME_LAYOUTS_DIR / 'taxonomy.html'
    terms = THEME_LAYOUTS_DIR / 'terms.html'
    term = THEME_LAYOUTS_DIR / 'term.html'

    # Rename taxonomy.html to term.html (singular)
    if taxonomy.exists():
        print(f'Renaming {taxonomy} to {term}')
        taxonomy.rename(term)

    # Rename terms.html to taxonomy.html
    if terms.exists():
        print(f'Renaming {terms} to {taxonomy}')
        terms.rename(taxonomy)

def rename_content_html_files():
    for path in THEME_LAYOUTS_DIR.rglob('content.html'):
        new_name = path.parent / ('_td-' + path.name)
        print(f'Renaming {path} to {new_name}')
        path.rename(new_name)

def scan_for_figure_shortcode(content_dir=Path('content')):
    # Scan content for old figure shortcode usage
    print("Scanning content for 'figure' shortcode usage...")
    for mdfile in content_dir.rglob('*.md'):
        with mdfile.open(encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if '{{< figure ' in line and 'caption=' not in line:
                    print(f'{mdfile}:{i}: Possible old figure shortcode usage: {line.strip()}')

def main():
    rename_taxonomy_files()
    rename_content_html_files()
    scan_for_figure_shortcode()

if __name__ == '__main__':
    main()