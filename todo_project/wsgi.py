import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

# Standard Django WSGI app
application = get_wsgi_application()

# Vercel requires this exact variable name
app = application  # Some Vercel setups need 'app'
handler = application  # Others need 'handler'