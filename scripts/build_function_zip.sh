#!/bin/bash
set -e

ZIP_FILE="function_source.zip"
rm -f $ZIP_FILE

# Install dependencies from pyproject.toml into package/
mkdir -p package
pip install --target ./package . 

# Copy source files
cp *.py ./package/
cp -r scripts ./package/

# Zip everything
cd package
zip -r ../$ZIP_FILE .
cd ..
echo "Created $ZIP_FILE"

