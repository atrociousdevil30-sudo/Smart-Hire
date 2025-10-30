""
WSGI config for SmartHire AI.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It exposes a module-level variable named
`application` which is the default WSGI application.
"""

import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

def get_wsgi_application():
    ""
    Get the WSGI application for this project.
    
    This function is separated to allow for potential pre-import
    hooks or other WSGI middleware to be wrapped around the application.
    """
    # Set the default settings module if not already set
    os.environ.setdefault('FLASK_APP', 'smarthire_ai.app')
    os.environ.setdefault('FLASK_ENV', 'production')
    
    # Import the Flask app after setting the environment variables
    from smarthire_ai.app import create_app
    
    # Create and return the Flask application
    return create_app()

# This is the WSGI application that will be used by the WSGI server
application = get_wsgi_application()

if __name__ == "__main__":
    # This block is used when running with python wsgi.py directly
    # It's not recommended for production use
    print("Starting development server...")
    application.run(host='0.0.0.0', port=5000)
