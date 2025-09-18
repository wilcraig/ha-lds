#!/bin/bash

# LDS Integration Card Installation Script
# This script copies the custom cards to the correct location in Home Assistant

echo "🏛️ LDS Integration - Card Installation Script"
echo "============================================="

# Check if we're in the right directory
if [ ! -f "custom_components/lds/manifest.json" ]; then
    echo "❌ Error: Please run this script from the ha-lds repository root directory"
    exit 1
fi

# Define paths
SOURCE_DIR="www"
TARGET_DIR="../../../www/community/ha-lds"

# Create target directory if it doesn't exist
echo "📁 Creating target directory: $TARGET_DIR"
mkdir -p "$TARGET_DIR"

# Copy card files
echo "📋 Copying custom card files..."
for file in "$SOURCE_DIR"/*.js; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        echo "   Copying $filename"
        cp "$file" "$TARGET_DIR/"
    fi
done

echo "✅ Card installation complete!"
echo ""
echo "🔧 Next Steps:"
echo "1. Add resources to your Lovelace configuration:"
echo "   - /local/community/ha-lds/lds-quote-card.js"
echo "   - /local/community/ha-lds/lds-scripture-card.js"
echo "   - /local/community/ha-lds/lds-come-follow-me-card.js"
echo "   - /local/community/ha-lds/lds-inspirational-card.js"
echo ""
echo "2. Restart Home Assistant"
echo "3. Clear your browser cache"
echo "4. Add the custom cards to your dashboard"
echo ""
echo "📖 See CARDS_SETUP.md for detailed configuration instructions"
