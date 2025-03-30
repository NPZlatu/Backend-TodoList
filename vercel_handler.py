import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

application = get_asgi_application()

def handler(request):
    """Serve requests using Django ASGI application."""
    from django.http import HttpResponse
    response = application(request)
    return HttpResponse(response.content)
