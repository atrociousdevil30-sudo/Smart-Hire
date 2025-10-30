"""
WSGI config for SmartHire AI.

This module contains the WSGI application for production deployment.
"""

import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

def get_wsgi_application():
    """
    Get the WSGI application for this project.
    """
    # Set environment variables
    os.environ.setdefault('FLASK_ENV', 'production')
    os.environ.setdefault('FLASK_APP', 'smarthire_ai.app')
    
    # Import the Flask app after setting the environment variables
    from smarthire_ai.app import app as application
    
    return application

# This is the WSGI application that will be used by the WSGI server
application = get_wsgi_application()

if __name__ == "__main__":
    # This block is used when running with python wsgi.py directly
    # It's not recommended for production use
    print("Starting development server...")
    application.run(host='0.0.0.0', port=5000)
