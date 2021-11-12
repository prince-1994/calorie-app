from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserProfileAPIViewTests(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_1 = get_user_model().objects.create_user('yuvraj', password='yuvraj123')
        cls.token_1 = Token.objects.create(user=cls.user_1)
        return super().setUpTestData()

    def test_user_profile_get(self):
        url = reverse('userprofile')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + UserProfileAPIViewTests.token_1.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    