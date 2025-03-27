"""Module with User Models"""

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom User model extending the base AbstractUser model to add extra
    fields.

    This model extends the default `AbstractUser` by adding an `email` field
    with a unique constraint. It also allows for many-to-many relationships
    with `Group` and `Permission` models to assign groups and permissions
    to users. This model overrides the default `__str__` method to return
    the username associated with the user profile.

    Fields:
        email (EmailField): A unique email address for the user. This is
                             in addition to the `username` field provided by
                             the base `AbstractUser` model.
        groups (ManyToManyField): A many-to-many relationship with the `Group`
                                  model. Allows a user to be assigned to
                                  multiple
                                  groups.
        user_permissions (ManyToManyField): A many-to-many relationship with
        the
                                            `Permission` model. Allows a user
                                            to have multiple permissions.
    """

    email = models.EmailField(unique=True)
    """
    The email field stores the user's email address. It is set to be unique, 
    meaning
    no two users can have the same email address. This field is in addition 
    to the
    default `username` field provided by `AbstractUser`.
    """

    groups = models.ManyToManyField(
        Group, related_name="customuser_set", blank=True
    )
    """
    A many-to-many relationship with the `Group` model. Groups allow you to 
    assign 
    users to multiple groups, making it easier to manage permissions. 
    The `blank=True` argument allows the field to be optional for users.
    """

    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_set", blank=True
    )
    """
    A many-to-many relationship with the `Permission` model. Permissions 
    grant users 
    specific rights in the system, such as adding or deleting objects.
    The `blank=True` argument allows the field to be optional for users.
    """

    def __str__(self):
        """
        Returns the username of the user. This method is overridden from the
        base `AbstractUser` model to return the `username` field, which is
        typically used as the user's unique identifier.

        Returns:
            str: The username of the user.
        """
        return str(self.username)
