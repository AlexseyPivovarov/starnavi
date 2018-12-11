from rest_framework.test import APITestCase

from .models import CustomUser


# Create your tests here.
class AuthTests(APITestCase):

    def setUp(self):
        self.credentials = {"username": "a.peevovarov@gmail.com", "password": "test@test"}
        CustomUser.objects.create_user(**self.credentials)

    def test_can_add_user(self):
        data = {"username": "1stpaninalexey@bigmir.com.ua", "password": "test@test"}
        response = self.client.post('/auth/register/', data=data)
        self.assertEqual(response.status_code, 201)

    def test_login_refresh(self):
        response = self.client.post('/auth/login/', data=self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "access")

        data = {'refresh': response.data['refresh']}
        response = self.client.post('/auth/login/refresh/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "access")
