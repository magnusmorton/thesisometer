from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
# Create your tests here.


class CountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("bob")
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)

    def test_can_post_count(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post('/graphs/api/wordcount/', {"count": 420}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_get_count(self):
        response = self.client.get('/graphs/api/wordcount/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
