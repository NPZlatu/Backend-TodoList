# your_app/tests/unit/test_models.py

from django.test import TestCase
from django.contrib.auth.models import User
from todo.models import Todo

class TodoModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_todo_creation(self):
        todo = Todo.objects.create(user=self.user, title="Sample Todo", description="Sample Description")
        self.assertEqual(todo.title, "Sample Todo Wrong")
