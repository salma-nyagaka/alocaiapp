import json
from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase


class BaseTestCase(TestCase):
    """Base test file to be used by other test files in the package"""

    def setUp(self):

        self.client = APIClient()

        # Access urls for testing
        self.create_game_url = reverse("create-game")

        self.payload = {
            "name": "test",
            "price": 11.1,
            "space": 1073741824
        }
