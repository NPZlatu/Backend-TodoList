"""
WSGI config for todo_project project.
Modified for Vercel deployment.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

# Django's standard WSGI application test
application = get_wsgi_application()

# Vercel requires this variable
handler = application  # Same as `app` if using Flask/FastAPI