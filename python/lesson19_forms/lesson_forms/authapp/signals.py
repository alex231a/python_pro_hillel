"""Module with signals"""

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """
    Signal handler that creates a UserProfile instance whenever a new User
    is created.

    Args:
        instance (User): The actual instance being saved.
        created (bool): A boolean indicating whether the instance was created.
    """
    if created:
        UserProfile.objects.create(user=instance) # pylint: disable=no-member


@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    """
    Signal handler that ensures the associated UserProfile is saved whenever
    a User instance is updated.

    Args:
        instance (User): The actual instance being saved.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
