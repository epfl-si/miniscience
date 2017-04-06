# (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author


class AuthorAPITestCase(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('root', 'admin@admin.com', 'admin123')
        self.client.login(username='root', password='admin123')

    def test_can_read_author(self):
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
