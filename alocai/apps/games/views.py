from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import GameSerializer
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
    """ Class to get game values """
    renderer_classes = (RequestJSONRenderer,)
    # serializer_class = GameSerializer

    def post(self, request):
        """ Method to get highest possible total value
        that fits given pen-drive space """

        params = request.query_params
        data = validate_params(params)

        return_message = {
            'message': data
        }
        return Response(return_message,
        status=status.HTTP_400_BAD_REQUEST)
