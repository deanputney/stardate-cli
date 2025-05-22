#!/bin/bash
# Script to create a release tarball for stardate-cli

VERSION="0.0.1"
RELEASE_DIR="dist/stardate-${VERSION}"
TARBALL="dist/stardate-${VERSION}.tar.gz"

# Create release directory structure
mkdir -p ${RELEASE_DIR}/test_data

# Copy files
cp stardate.py README.md ${RELEASE_DIR}/
cp test_data/*.txt ${RELEASE_DIR}/test_data/

# Create tarball
cd dist
tar -czvf stardate-${VERSION}.tar.gz stardate-${VERSION}
cd ..

# Display SHA256 hash
echo "SHA256 hash for Formula/stardate.rb:"
sha256sum ${TARBALL}

echo ""
echo "Tarball created at: ${TARBALL}"
echo "Upload this file to GitHub as release v${VERSION}"