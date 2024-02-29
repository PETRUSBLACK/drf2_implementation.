from django.test import TestCase
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .serializer import TaskSerializer, Task

class YourModelRetrieveAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.your_model = Task.objects.create(title='Test', description='Test Description', Status_options='completed')

    def test_retrieve_api_view(self):
        response = self.client.get(f'/task/Task/{self.Task.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = TaskSerializer(instance=self.Task).data
        self.assertEqual(response.data, expected_data)
In 
