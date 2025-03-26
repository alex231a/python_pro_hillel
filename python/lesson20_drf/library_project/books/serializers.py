"""Module containing the serializer for the Book model."""
from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer converts Book model instances into JSON format and vice
    versa.

    Meta:
        model (Book): The model that is being serialized.
        fields (str or list): Specifies which fields should be included in
        the serialization.
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class."""
        model = Book
        fields = '__all__'
