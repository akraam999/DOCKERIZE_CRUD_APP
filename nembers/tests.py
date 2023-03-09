from nembers.models import *
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class testStudent(APITestCase):
    def setUp(self):
        self.student1 = Student.objects.create(first_name="simon",last_name="badr",email="simon@gmail.com",password="1234",classLevel=2)
        self.student2 = Student.objects.create(first_name="sofia",last_name="moufid",email="sofia@gmail.com",password="1234",classLevel=1)
    def test_list_students(self):
        url = reverse('get_students')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(len(response.data), 2)
