#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Export environment variables from .env manually (or rely on python-dotenv in app.py)
export FLASK_APP=app.py
export FLASK_ENV=production

# Run Gunicorn
exec gunicorn app:app \
    --bind 0.0.0.0:5000 \
    --workers 3 \
    --timeout 120 \
    --log-level info \
    --access-logfile - \
    --error-logfile -
