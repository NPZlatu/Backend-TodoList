import os
from django.core.wsgi import get_wsgi_application
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

application = get_wsgi_application()

def handler(request):
    """Handle incoming requests to the Django application."""
    # Create a WSGI environment for the request
    environ = request.environ
    environ['wsgi.input'] = request.body
    environ['REQUEST_METHOD'] = request.method
    environ['PATH_INFO'] = request.path
    environ['QUERY_STRING'] = request.query_string

    # Ensure the request is passed to Django's application
    response = application(environ, start_response)

    return HttpResponse(response)

def start_response(status, response_headers, exc_info=None):
    """A simple WSGI start_response function."""
    return None
