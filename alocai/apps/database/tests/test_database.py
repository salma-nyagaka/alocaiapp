import json
from rest_framework import status

from .base_file import BaseTestCase


class TestDatabaseApi(BaseTestCase):
    """Class to test the db connectivity"""

    def test_create_order(self):
        """Test if connection is successful"""

        response = self.client.get(self.database_connection_url, format="json")
        response_data =  json.loads(response.content)
        self.assertEqual(response_data['message'], {"database": "healthy"})
