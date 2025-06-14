#!/bin/bash

# Directory where your content lives
CONTENT_DIR="/Volumes/DevProjects/greenorbitspace/docsy/userguide/content/en/docs/notion-handbook"
SHORTCODES_DIR="layouts/_shortcodes"

echo "🔍 Scanning for shortcodes in: $CONTENT_DIR"
echo "🔧 Validating against:         $SHORTCODES_DIR"

# Find all shortcode names ({{< name >}} or {{% name %}})
grep -rhoE '{{[%<] *([a-zA-Z0-9_-]+)' "$CONTENT_DIR" | \
  sed -E 's/{{[%<] *//g' | sort | uniq > /tmp/used_shortcodes.txt

echo -e "\n📄 Shortcodes using {{< >}} syntax:"
cat /tmp/used_shortcodes.txt

echo -e "\n🧩 Checking for missing shortcode templates..."

MISSING=false
while read -r shortcode; do
  if [ ! -f "$SHORTCODES_DIR/$shortcode.html" ]; then
    echo "❌ Missing shortcode: $shortcode"
    echo "   ↳ Used in:"
    
    # Get files that use this shortcode
    files=$(grep -rl "{{% *$shortcode" "$CONTENT_DIR")
    echo "$files"

    # Fix shortcode in each file
    echo "🔧 Replacing shortcode with fallback HTML..."
    for file in $files; do
      sed -E -i '' "s#{{% *$shortcode \"([^\"]*)\" *%}}#<div class=\"alert alert-warning\"><strong>Note:</strong> $shortcode: \1</div>#g" "$file"
    done

    echo "✅ Replaced in affected files."
    echo ""
    MISSING=true
  fi
done < /tmp/used_shortcodes.txt

if [ "$MISSING" = false ]; then
  echo "✅ All shortcodes used are defined in $SHORTCODES_DIR/"
else
  echo "⚠️ Some shortcodes were missing and have been patched in content files."
fi