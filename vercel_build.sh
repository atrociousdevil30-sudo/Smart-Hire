#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install spacy model
python -m spacy download en_core_web_sm

# Create necessary directories
mkdir -p static/uploads
mkdir -p instance

# Set environment variables
export FLASK_APP=smarthire_ai.app
export FLASK_ENV=production

# Run database migrations (if any)
# flask db upgrade

echo "Build completed successfully"
