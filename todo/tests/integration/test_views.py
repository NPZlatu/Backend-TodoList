# your_app/tests/integration/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class TodoAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_todo(self):
        url = '/api/todos/'
        data = {"title": "New Todo", "description": "Test Description", "completed": False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
