from rest_framework.test import APITestCase, RequestsClient, APIClient

from curent_auth.models import CustomUser
from .models import Posts
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import requests


# Create your tests here.
class PostsTests(APITestCase):

    def setUp(self):
        self.credentials = {"username": "a.peevovarov@gmail.com", "password": "test@test"}
        user = CustomUser.objects.create_user(**self.credentials)
        response = self.client.post('/auth/login/', data=self.credentials, follow=True)
        self.access = response.data['access']
        Posts.objects.create(title='test', body='this is test', user=user)

    def test_posts_like(self):
        post = Posts.objects.get(title='test')
        self.client.credentials(HTTP_AUTHORIZATION=" ".join(["Bearer", self.access]))
        response = self.client.patch(f'/posts/like/{post.title}/')
        post.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(post.like, 1)

    def test_posts_unlike(self):
        post = Posts.objects.get(title='test')
        self.client.credentials(HTTP_AUTHORIZATION=" ".join(["Bearer", self.access]))
        response = self.client.patch(f'/posts/unlike/{post.title}/')
        post.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(post.unlike, 1)

    def test_posts_add(self):
        self.client.credentials(HTTP_AUTHORIZATION=" ".join(["Bearer", self.access]))
        data = {'title': 'test2', 'body': 'this is test'}
        response = self.client.post(f'/posts/add/',data=data)
        self.assertEqual(response.status_code, 201)
        # post = Posts.objects.get(title=
        try:
            Posts.objects.get(title='test2')
        except:
            self.assertTrue(False)
