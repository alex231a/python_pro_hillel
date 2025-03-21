"""Module defining models for the advertisement system."""

from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    """
    Represents a user's profile with additional details.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(
        upload_to='avatars',
        blank=True,
        null=True,
        max_length=100,
    )

    def __str__(self):
        """Returns the username associated with the profile."""
        return self.user.username  # pylint: disable=no-member
