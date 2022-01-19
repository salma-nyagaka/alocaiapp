from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import GameSerializer, GameValueSerializer
from ...helpers.constants import SUCCESS_MESSAGE
from ...helpers.renderers import RequestJSONRenderer

from .helpers.validate_params import validate_params


class GamesApiView(generics.GenericAPIView):
    """Class to add order items"""

    renderer_classes = (RequestJSONRenderer,)
    serializer_class = GameSerializer

    def post(self, request):
        """Method to add a new game"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return_message = {
            "message": SUCCESS_MESSAGE.format("The game has been created"),
            "data": serializer.data,
        }
        return Response(return_message, status=status.HTTP_201_CREATED)


class PenDriveApiView(generics.GenericAPIView):
    """Class to get game values"""

    renderer_classes = (RequestJSONRenderer,)
    serializer_class = GameValueSerializer

    def get(self, request):
        """Method to get highest possible total value
        that fits given pen-drive space"""

        params = request.query_params
        data = validate_params(params)
        serializer = self.serializer_class(data[0], many=True)

        return_message = {
            "message": SUCCESS_MESSAGE.format("The game values have been fetched"),
            "data":{
            "games": serializer.data,
            "total_space": data[1],
            "empty_space": data[2],
            }
        }
        return Response(return_message, status=status.HTTP_200_OK)
