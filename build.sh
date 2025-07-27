#!/usr/bin/env bash
# This script is used to build the Django project for deployment.
# It collects static files and applies migrations.
set -o errexit  # Exit immediately if a command exits with a non-zero status.

pip install -r requirements.txt  # Install dependencies
python manage.py collectstatic --noinput  # Collect static files
python manage.py migrate  # Apply database migrations
echo "Build completed successfully."
