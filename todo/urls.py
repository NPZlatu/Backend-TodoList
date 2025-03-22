from django.urls import path
from .views import RegisterView, LoginView, LogoutView, TodoListCreateView, TodoUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # the following path handles both creating a todo and listing all todos
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoUpdateView.as_view(), name='todo-detail'),
]