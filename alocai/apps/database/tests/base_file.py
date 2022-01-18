import json
from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase


class BaseTestCase(TestCase):
    """Base test file to be used by other test files in the package"""

    def setUp(self):

        self.client = APIClient()

        # Access urls for testing
        self.database_connection_url = reverse("database-connection")
        