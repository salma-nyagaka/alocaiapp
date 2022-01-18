from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    """ Serialize a game's data"""

    # Ensure that name is unique, does not exist,
    # and cannot be left be blank
    name = serializers.RegexField(
        regex='[a-zA-Z0-9 ]',
        min_length=4,
        max_length=30,
        required=True,
        validators=[UniqueValidator(
            queryset=Game.objects.all(),
            message='The name already exists. Kindly try another.'
        )],
        error_messages={
            "blank": "Name cannot be empty.",
            "min_length": "Name should have more than 4 characters",
            "max_length": "Name should have less than  characters",

        },
    )
    # Ensure that price cannot be left be
    # blank and is a positive number
    price = serializers.RegexField(
        regex='[+-]?([0-9]*[.])?[0-9]+',
        required=True,
        error_messages={
            "blank": "Price cannot be empty.",
            "invalid": "Price should be a positive number",
        },
    )
    # Ensure that space cannot be left be
    # blank and is a positive number
    space = serializers.RegexField(
        regex='^[1-9]+[0-9]*$',
        required=True,
        error_messages={
            "blank": "Space cannot be empty.",
            "invalid": "Space should be a positive number",
        },
    )

    class Meta:
        model = Game
        fields = ['name', 'price', 'space']

        extra_kwargs = {"name": {"error_messages": {
            "blank": "Give yourself a username"}}}
