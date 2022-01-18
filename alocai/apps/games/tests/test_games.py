import json
from rest_framework import status

from .base_file import BaseTestCase


class TestCreateGameApi(BaseTestCase):
    """Class to test the game API"""

    def test_create_order(self):
        """Test to create a game"""

        response = self.client.post(self.create_game_url, data=self.payload, format="json")
        response_data =  json.loads(response.content)
        self.assertEqual(response_data['message'], "The game has been created successfully")
