from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from .models import User


class UserAPIViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123',
            phone='08000000000',
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='otheruser@example.com',
            password='testpass123',
            phone='08000000001',
        )

    def test_user_list_returns_active_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['username'], 'testuser')
        self.assertEqual(response.data[1]['username'], 'otheruser')

    def test_profile_requires_authentication(self):
        url = reverse('profile')
        response = self.client.get(url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_profile_returns_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'testuser@example.com')
        self.assertEqual(response.data['phone'], '08000000000')

    def test_homepage_returns_welcome_message(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Welcome to Easy Buy', response.content.decode())
        self.assertIn('/api/users/', response.content.decode())
