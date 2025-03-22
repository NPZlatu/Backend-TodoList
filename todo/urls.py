from django.urls import path
from .views import RegisterView, LoginView, LogoutView, TodoListCreateView, TodoUpdateDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # the following path handles both creating a todo and listing all todos
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    # the following path handles both updating and deleting a todo
    path('todos/<int:pk>/', TodoUpdateDeleteView.as_view(), name='todo-detail'),
]