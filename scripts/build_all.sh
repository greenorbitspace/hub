#!/bin/bash
# build_all.sh
# Modular Hugo build for Green Orbit documentation

set -e

ROOT_DIR=$(pwd)
MODULES_DIR="$ROOT_DIR/modules"
PUBLIC_DIR="$ROOT_DIR/public"

echo "Starting build for all modules..."

# Initialize Hugo modules if go.mod missing
if [ ! -f go.mod ]; then
    echo "Initializing Hugo modules..."
    hugo mod init github.com/greenorbitspace/docs
fi

# Fetch required Hugo modules
echo "Fetching Hugo modules..."
hugo mod get github.com/google/docsy
hugo mod get github.com/FortAwesome/Font-Awesome
hugo mod get github.com/twbs/bootstrap
hugo mod tidy

# Clear previous generated resources
rm -rf resources/_gen
rm -rf modules/*/resources/_gen

# Ensure public folder exists
mkdir -p "$PUBLIC_DIR"

# Build each module
for module_path in "$MODULES_DIR"/*; do
    if [ -d "$module_path" ]; then
        module_name=$(basename "$module_path")
        dest="$PUBLIC_DIR/$module_name"
        echo "Building module: $module_name -> $dest"

        hugo \
            --source "$module_path" \
            --destination "$dest" \
            --cleanDestinationDir \
            --minify \
            --enableGitInfo \
            --ignoreCache
    fi
done

echo "✅ All modules built successfully!"