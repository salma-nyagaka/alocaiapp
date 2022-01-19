import json
from rest_framework import status

from .base_file import BaseTestCase
from games.apps import GamesConfig


class TestCreateGameApi(BaseTestCase):
    """Class to test the game API"""

    def test_apps(self):
        """Test apps file"""
        self.assertEqual(GamesConfig.name, "games")

    def test_create_order(self):
        """Test to create a game"""

        response = self.create_game()
        response_data = json.loads(response.content)
        self.assertEqual(
            response_data["message"], "The game has been created successfully"
        )

    def test_get_value(self):
        """Test to get game values"""

        self.create_game()
        response = self.client.get(
            self.game_value_url,
            data=self.payload,
            format="json",
            **{"QUERY_STRING": "pen_drive_space=100"},
        )
        response_data = json.loads(response.content)

        self.assertEqual(
            response_data["message"], "The game values have been fetched successfully"
        )

    def test_get_value_no_params(self):
        """Test if no params"""

        self.create_game()
        response = self.client.get(
            self.game_value_url, data=self.payload, format="json"
        )
        response_data = json.loads(response.content)
        self.assertEqual(
            response_data["error"], ["pen_drive_space in params is required."]
        )

    def test_get_value_no_params_value(self):
        """Test if params has no value"""

        self.create_game()
        response = self.client.get(
            self.game_value_url,
            data=self.payload,
            format="json",
            **{"QUERY_STRING": "pen_drive_space="},
        )
        response_data = json.loads(response.content)
        self.assertEqual(
            response_data["error"],
            [
                "pen_drive_space value in params cannot be empty. Kindly pass a positive integer"
            ],
        )

    def test_get_value_params_with_negative_value(self):
        """Test params with negative value"""

        self.create_game()
        response = self.client.get(
            self.game_value_url,
            data=self.payload,
            format="json",
            **{"QUERY_STRING": "pen_drive_space=-10"},
        )
        response_data = json.loads(response.content)
        self.assertEqual(
            response_data["error"],
            ["pen_drive_space value in params has to be a positive number"],
        )
