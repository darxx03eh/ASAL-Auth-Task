from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import User
class LoginAPITestCase(APITestCase):
    def setUp(self):
        self.username = 'darawsheh'
        self.password = 'darawsheh'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.url = reverse('login')

    def test_login(self):
        response = self.client.post(self.url, data={
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LogOutAPITestCase(APITestCase):
    def setUp(self):
        self.username = 'darawsheh'
        self.password = 'darawsheh'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.login = reverse('login')
        self.logout = reverse('logout')

    def test_logout(self):
        user = self.client.post(self.login, data={
            'username': self.username,
            'password': self.password
        })
        user_data = user.json()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_data.get('access')}')
        response = self.client.post(self.logout, data={
            'refresh': user_data.get('refresh'),
        })
        self.assertEqual(user.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SignUpAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse('signup')
    def test_signup(self):
        payload = {
            "first_name": "Mahmoud",
            "last_name": "Darawsheh",
            "username": "darxx03eh",
            "email": "darxx03eh@mail.ru",
            "password": "123456789+-",
            "phone_number": "+970568249300"
        }

        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)