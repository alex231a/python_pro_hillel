"""Module defining models for the advertisement system."""

from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    """
    Represents a user's profile with additional details.

    Attributes:
        user (OneToOneField): Links the profile to the Django User model.
        phone_number (CharField): Stores the user's phone number.
        address (TextField): Stores the user's address.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        """Returns the username associated with the profile."""
        return self.user.username  # pylint: disable=no-member


class Category(models.Model):
    """
    Represents a category of advertisements.

    Attributes:
        name (CharField): The name of the category (unique).
        description (TextField): Optional description of the category.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def active_ads_count(self):
        """
        Returns the number of active advertisements in this category.

        DRY Principle: Instead of writing a custom query elsewhere,
        we use the related_name='ads' to filter the ads directly.
        """
        return self.ads.filter(is_active=True).count()

    def __str__(self):
        """Returns the name of the category."""
        return self.name


class Ad(models.Model):
    """
    Represents an advertisement posted by a user.

    Attributes:
        title (CharField): The title of the advertisement.
        description (TextField): The full description of the ad.
        price (DecimalField): The price of the advertised item.
        created_at (DateTimeField): Timestamp of when the ad was created.
        updated_at (DateTimeField): Timestamp of the last update.
        is_active (BooleanField): Indicates if the ad is currently active.
        user (ForeignKey): Links the ad to the user who created it.
        category (ForeignKey): Links the ad to a category.
    """

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='ads')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='ads'
    )

    def short_description(self):
        """
        Returns a shortened version of the advertisement's description.

        DRY Principle: Instead of manually truncating descriptions elsewhere,
        we use a single method that ensures consistent truncation logic.
        """
        if not self.description:
            return "No description available."
        return str(self.description)[:100] + (
            "..." if len(str(self.description)) > 100 else ""
        )

    def check_expiration(self):
        """
        Automatically deactivates the advertisement if it is older than 30 days.

        DRY Principle: This method allows consistent expiration logic
        instead of writing similar expiration checks in multiple places.
        """
        if self.is_active and self.created_at < timezone.now() - timedelta(
                days=30):
            self.is_active = False
            self.save(update_fields=['is_active'])

    def comment_count(self):
        """
        Returns the number of comments on this advertisement.

        DRY Principle: Instead of defining a separate static method in Comment,
        this method uses the related_name='comments' to count associated objects.
        """
        return self.comments.count()

    def clean(self):
        """
        Ensures that the advertisement has a valid price.

        Raises:
            ValidationError: If the price is zero or negative.
        """
        if self.price <= 0:
            raise ValidationError("Price must be greater than zero.")

    def __str__(self):
        """Returns the title of the advertisement."""
        return self.title


class Comment(models.Model):
    """
    Represents a comment made on an advertisement.

    Attributes:
        content (TextField): The text content of the comment.
        created_at (DateTimeField): Timestamp of when the comment was created.
        ad (ForeignKey): Links the comment to an advertisement.
        user (ForeignKey): Links the comment to the user who made it.
    """

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a formatted string representation of the comment."""
        return f'Comment by {self.user.username} on {self.ad.title}'  # pylint: disable=no-member
