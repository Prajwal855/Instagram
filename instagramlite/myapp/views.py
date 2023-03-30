from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from myapp import serializers


# Create your views here.

class HelloAPIView(APIView):
    """Test API VIEW"""
    serializer_class = serializers.Helloserializer

    def get(self, request, format=None):
        """Returns a list of APIView Feature"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is Similar to a traditional Django View',
            'Gives You the Most Control Over you application logic',
            'Is Mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello Message with our Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self, request, pk=None):
        """Handle Updating An object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle Partially Updating An object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle Deleting an  Object"""
        return Response({'method': 'DELETE'})


class HelloViewSets(viewsets.ViewSet):
    """Test API View sets"""
    serializer_class = serializers.Helloserializer

    def list(self, request):
        """Return a Hello Message"""
        a_viewset = [
            'Users Action (list, create, retrieve, update, partial_update',
            'Automatically maps to URLs using routers',
            'provides more functionality to test code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle Getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle Updating an Object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle Partially Updating an Object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle Delete an Object"""
        return Response({'http_method': 'DELETE'})