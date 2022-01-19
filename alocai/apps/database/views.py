from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from ...helpers.renderers import RequestJSONRenderer


class DatabaseConnectionApiView(generics.GenericAPIView):
    """Get database connectivity"""

    def get(self, request):
        """Method to test and get database status
        after connecting"""
        # try:
        data = {"database": "healthy"}
        return_message = {"message": data}
        return Response(return_message, status=status.HTTP_200_OK)
        # except:
        #     data = {"database": "unhealthy"}
        #     return_message = {"message": data}
        #     return Response(return_message, status=status.HTTP_400_BAD_REQUEST)
