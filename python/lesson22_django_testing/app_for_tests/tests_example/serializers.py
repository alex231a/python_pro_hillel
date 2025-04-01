"""
This module defines serializers for handling task and user data in a Django
REST Framework (DRF) API.

The serializers included:
- `TaskSerializer`: Serializes `Tasks` model data and validates the
`due_date` field.
- `UserSerializer`: Serializes `User` model data from Django's
authentication system.
- `NestedTaskSerializer`: Extends `TaskSerializer` to include user details
via a nested representation.
"""

import datetime

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Tasks` model.

    Fields:
        - `title`: The title of the task.
        - `description`: Optional task description.
        - `due_date`: The deadline for task completion.

    Validation:
        - Ensures that `due_date` is not set in the past.
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta for TaskSerializer."""
        model = Tasks
        fields = ('title', 'description', 'due_date')

    def validate_due_date(self, value):
        """
        Validate that the due date is not set in the past.

        Args:
            value (datetime.date): The input due date.

        Returns:
            datetime.date: The validated due date.

        Raises:
            serializers.ValidationError: If the due date is in the past.
        """
        if value and value < datetime.date.today():
            raise serializers.ValidationError(
                "Due date cannot be in the past.")
        return value


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the `User` model.

    Fields:
        - `id`: The unique identifier of the user.
        - `username`: The username of the user.
        - `email`: The email address of the user.
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta for UserSerializer."""
        model = User
        fields = ('id', 'username', 'email')


class NestedTaskSerializer(serializers.ModelSerializer):
    """
    Serializer for tasks that includes user details as a nested representation.

    Fields:
        - `title`: The title of the task.
        - `description`: Optional task description.
        - `due_date`: The deadline for task completion.
        - `user`: Nested `UserSerializer` containing user details.
    """
    user = UserSerializer()

    class Meta:  # pylint: disable=too-few-public-methods
        """Class Meta for NestedTaskSerializer."""
        model = Tasks
        fields = ('title', 'description', 'due_date', 'user')
