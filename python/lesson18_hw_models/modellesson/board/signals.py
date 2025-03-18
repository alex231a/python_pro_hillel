"""Module for signals"""

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Ad


@receiver(post_save, sender=Ad)
def send_ad_creation_email(sender, instance, created, **kwargs):
    """Function to send an email to an ad"""
    if created:
        send_mail(
            'Your ads was created!',
            f'Ads "{instance.title}" was created! {sender}{kwargs}',
            'no-reply@board.com',
            [instance.user.email],
            fail_silently=True,
        )


@receiver(post_save, sender=Ad)
def deactivate_expired_ads(sender, instance, **kwargs):
    """Function to deactivate expired ads"""

    print(f"{sender}{kwargs} is now necessary in this case")

    post_save.disconnect(deactivate_expired_ads,
                         sender=Ad)
    instance.check_expiration()
    post_save.connect(deactivate_expired_ads, sender=Ad)
