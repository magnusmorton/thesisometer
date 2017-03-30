from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import WordCount
# Create your tests here.


class CountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("bob", password="bob")
        self.client = APIClient()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_can_post_count(self):
        response = self.client.post('/graphs/api/wordcount/', {"count": 420}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_get_count(self):
        response = self.client.get('/graphs/api/wordcount/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_one_count_for_day(self):
        WordCount(count=420, date="2017-01-20", user=self.user).save()
        WordCount(count=500, date="2017-01-20", user=self.user).save()
        counts = WordCount.objects.filter(date="2017-01-20")
        self.assertEqual(len(counts), 1)

    def test_can_make_multiple_counts(self):
        WordCount(count=420, date="2017-01-20", user=self.user).save()
        WordCount(count=500, date="2017-01-21", user=self.user).save()
        counts = WordCount.objects.all()
        self.assertEqual(len(counts), 2)

    def test_filtering_reduces_number_of_counts(self):
        WordCount(count=420, date="2017-01-20", user=self.user).save()
        WordCount(count=500, date="2017-01-21", user=self.user).save()
        WordCount(count=600, date=date.today().isoformat(), user=self.user).save()
        response = self.client.get('/graphs/api/users/?date_range=month', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]['counts']), 1)

    # TODO: improve these tests

    def test_filtering_quarter(self):
        WordCount(count=420, date="2016-01-20", user=self.user).save()
        WordCount(count=600, date=date.today().isoformat(), user=self.user).save()
        response = self.client.get('/graphs/api/users/?date_range=quarter', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]['counts']), 1)

    def test_filtering_year(self):
        WordCount(count=420, date="2016-01-20", user=self.user).save()
        WordCount(count=600, date=date.today().isoformat(), user=self.user).save()
        response = self.client.get('/graphs/api/users/?date_range=year', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]['counts']), 1)

    def test_filtering_all(self):
        WordCount(count=420, date="2016-01-20", user=self.user).save()
        WordCount(count=500, date="2017-01-21", user=self.user).save()
        WordCount(count=600, date=date.today().isoformat(), user=self.user).save()
        response = self.client.get('/graphs/api/users/?date_range=all', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]['counts']), 3)
