from django.contrib.auth import get_user_model
from django.db.models.functions import Random
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from app.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('user-list')
        self.detail_url = reverse('user-detail', args=[1])
        self.create_url = reverse('user-create')
        self.update_url = reverse('user-update', args=[1])
        User = get_user_model()
        self.admin_user = User.objects.create_superuser(username="poojab", first_name="pooja", last_name="bankapur",
                                                   email='pooja@user.com', password='pooja123')
        self.client.login(username="poojab", password="pooja123")

    def test_user_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_create_post(self):
        User.objects.create_user(username="test_test", first_name="test65", last_name="test87",
                                        email='normal123@user.com',
                                        password='test245')

        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_post(self):
        user = User.objects.get(username="poojab")
        user.first_name = "pooja_updated"
        user.save()
        response = self.client.post(self.update_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

