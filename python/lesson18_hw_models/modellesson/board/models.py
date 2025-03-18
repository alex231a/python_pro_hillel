"""Module with models"""

from datetime import timedelta

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    """Class model for user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username  # pylint: disable=no-member


class Category(models.Model):
    """Class model for category"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def active_ads_count(self):
        """Method to get active ads count for category"""
        ads_queryset = self.ads.filter(is_active=True)
        return ads_queryset.count()

    def __str__(self):
        return f"{self.name}"


class Ad(models.Model):
    """Class model for ad"""
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='ads')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='ads')

    def short_description(self):
        """Method to get short description for ad"""
        return str(self.description)[:100] + (
            '...' if len(str(self.description)) > 100 else '')

    def check_expiration(self):
        """Method to check expiration for ad"""
        if self.is_active and self.created_at < timezone.now() - timedelta(
                days=30):
            self.is_active = False
            self.save(update_fields=['is_active'])

    def clean(self):
        """Method to clean ad"""
        if self.price <= 0:
            raise ValidationError('Price must be greater than zero.')

    def __str__(self):
        """Method to get string for ad"""
        return f"{self.title}"


class Comment(models.Model):
    """Class model for comment"""
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE,
                           related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.ad.title}' # pylint: disable=no-member

    @staticmethod
    def count_comments(advertisement):
        """Method to count comments for ad"""
        return advertisement.comments.count()
