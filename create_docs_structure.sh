#!/bin/bash
# create_greenorbit_docs_modular.sh
# Creates the modular Hugo Docsy structure inside existing docs/ folder

set -e

ROOT_DIR="docs"

echo "Creating modular structure inside $ROOT_DIR..."

# 1. Themes folder (placeholder for submodule)
mkdir -p "$ROOT_DIR/themes/docsy"

# 2. Shared theme
mkdir -p "$ROOT_DIR/shared-theme/layouts/partials"
mkdir -p "$ROOT_DIR/shared-theme/assets/css"

# Create placeholder header/footer/custom CSS
echo "<!-- Header HTML -->" > "$ROOT_DIR/shared-theme/layouts/partials/header.html"
echo "<!-- Footer HTML -->" > "$ROOT_DIR/shared-theme/layouts/partials/footer.html"
echo "/* Custom CSS */" > "$ROOT_DIR/shared-theme/assets/css/custom.css"

# 3. Modules
for module in handbook ims glossary; do
    echo "Creating module: $module"
    mkdir -p "$ROOT_DIR/modules/$module/content"
    mkdir -p "$ROOT_DIR/modules/$module/data"

    # Create config.toml placeholder
    cat <<EOL > "$ROOT_DIR/modules/$module/config.toml"
# Config for $module
baseURL = "https://$module.example.com"
title = "Green Orbit $module"
theme = "docsy"
enableGitInfo = true
languageCode = "en-us"

[params]
  docsVersion = "v1.0"
  highlightStyle = "monokai"
  favicon = "/images/favicon.png"

[menu]
  # Add module-specific menu items here
EOL

    # Create _index.md
    echo -e "---\ntitle: \"$module Home\"\nweight: 1\n---\n\nWelcome to the $module module." > "$ROOT_DIR/modules/$module/content/_index.md"
done

# 4. Create example content for handbook and ims
echo -e "---\ntitle: \"Company Policies\"\nweight: 2\n---\n\nExample policies content." > "$ROOT_DIR/modules/handbook/content/policies.md"
echo -e "---\ntitle: \"Procedures\"\nweight: 3\n---\n\nExample procedures content." > "$ROOT_DIR/modules/handbook/content/procedures.md"
echo -e "---\ntitle: \"Quality Policy\"\nweight: 2\n---\n\nExample IMS quality policy content." > "$ROOT_DIR/modules/ims/content/quality-policy.md"
echo -e "---\ntitle: \"Processes\"\nweight: 3\n---\n\nExample IMS processes content." > "$ROOT_DIR/modules/ims/content/processes.md"

# 5. Scripts folder and build_all.sh
mkdir -p "$ROOT_DIR/scripts"
cat <<'EOL' > "$ROOT_DIR/scripts/build_all.sh"
#!/bin/bash
set -e
for module in ../modules/*; do
    echo "Building $module..."
    hugo --source "$module" --themesDir ../themes --destination "../public/$(basename $module)"
done
EOL
chmod +x "$ROOT_DIR/scripts/build_all.sh"

# 6. README.md placeholder
echo "# Green Orbit Docs" > "$ROOT_DIR/README.md"

# 7. Netlify.toml placeholder
cat <<EOL > "$ROOT_DIR/netlify.toml"
# Netlify multi-site deploy placeholder
[build]
  command = "bash scripts/build_all.sh"
  publish = "public"
EOL

echo "Modular Hugo Docsy structure created inside $ROOT_DIR!"