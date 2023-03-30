from rest_framework import serializers


class Helloserializer(serializers.Serializer):
    """Serializes a name field for testing our APIView """
    name = serializers.CharField(max_length=64)