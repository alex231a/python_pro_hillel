"""
Serializers for User and Tasks models in Django REST framework.

This module defines serializers for the User model (from Django's built-in
auth system)
and the Tasks model (from the tests_example application).
Serializers convert model instances into JSON representations and vice versa.

Usage:
- `UserSerializer`: Serializes User model fields such as `id`, `username`,
and `email`.
- `NestedTaskSerializer`: Serializes the Tasks model, including a nested
User representation.

Example:
    When retrieving task data via an API, the response will include task
    details
    along with user details in a nested format.
"""

from django.contrib.auth.models import User
from rest_framework import serializers

from tests_example.models import Tasks


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the built-in Django User model.
    Converts User model instances to JSON format.py
    """

    # pylint: disable=too-few-public-methods
    class Meta:
        """Class Meta for UserSerializer."""
        model = User
        fields = ('id', 'username', 'email')


class NestedTaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tasks model, including a nested User representation.
    This allows API responses to contain detailed user information alongside
    task data.
    """
    user = UserSerializer()

    # pylint: disable=too-few-public-methods
    class Meta:
        """Class Meta for NestedTaskSerializer."""
        model = Tasks
        fields = ('title', 'description', 'due_date', 'user')
