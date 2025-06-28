#!/bin/bash

# Exit on error
set -e

# Upgrade pip and tools
echo "Upgrading pip and tools..."
pip install --upgrade pip setuptools wheel

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "Creating directories..."
mkdir -p instance
mkdir -p static
mkdir -p templates

# Initialize database
echo "Initializing database..."
flask db upgrade

# Set proper permissions
echo "Setting permissions..."
chmod -R 755 instance
chmod -R 755 static
chmod -R 755 templates

# Clean up
echo "Cleaning up..."
rm -rf __pycache__
find . -name "__pycache__" -exec rm -rf {} +

# Show success message
echo "Build completed successfully!"