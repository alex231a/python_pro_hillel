"""Module for defining Django signals.

This module contains signal handlers that are triggered when specific
database events occur in the 'board' application.

Signals are used to:
- Send notifications when a new advertisement is created.
- Automatically deactivate expired ads.

Django's signal framework helps decouple components by allowing
certain functions to execute automatically when model events occur.
"""

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Ad


@receiver(post_save, sender=Ad)
def send_ad_creation_email(sender, instance, created, **kwargs):
    """
    Sends an email notification when a new advertisement (Ad) is created.

    This function listens to the `post_save` signal for the `Ad` model.
    If a new ad is created (`created=True`), an email notification
    is sent to the user who posted the ad.

    Args:
        sender (type): The model class that sent the signal (`Ad` in this case).
        instance (Ad): The specific instance of `Ad` that was saved.
        created (bool): Indicates whether the instance was newly created.
        **kwargs: Additional keyword arguments passed by the signal.

    Email Details:
        - Subject: "Your ad was created!"
        - Message: Confirmation message including the ad title.
        - Sender Email: 'no-reply@board.com'
        - Recipient Email: The email of the user who posted the ad.
    """
    if created:
        send_mail(
            subject='Your ad was created!',
            message=f'Ad "{instance.title}" has been successfully created!',
            from_email='no-reply@board.com',
            recipient_list=[instance.user.email],
            fail_silently=True,  # Prevents email failures from breaking execution
        )


@receiver(post_save, sender=Ad)
def deactivate_expired_ads(sender, instance, **kwargs):
    """
    Automatically deactivates ads that have expired.

    This function listens to the `post_save` signal for the `Ad` model.
    After an ad is saved, it checks if the ad has expired (older than 30 days).
    If expired, the ad is marked as inactive.

    Args:
        sender (type): The model class that sent the signal (`Ad` in this case).
        instance (Ad): The specific instance of `Ad` that was saved.
        **kwargs: Additional keyword arguments passed by the signal.

    Handling Signal Reconnection:
        - The signal is temporarily disconnected before calling `check_expiration()`
          to prevent recursive signal triggering.
        - After processing, the signal is reconnected.
    """
    print(f"Processing post-save signal for {sender}: {kwargs}")

    # Temporarily disconnect the signal to prevent infinite loops
    post_save.disconnect(deactivate_expired_ads, sender=Ad)

    # Check if the ad is expired and deactivate if necessary
    instance.check_expiration()

    # Reconnect the signal after processing
    post_save.connect(deactivate_expired_ads, sender=Ad)
