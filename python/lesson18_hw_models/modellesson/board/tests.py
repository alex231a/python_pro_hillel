"""Module for testing models and signals in the board app.

This module contains unit tests for:
- Validating ad price constraints
- Ensuring ads expire correctly after 30 days

The tests use Django's `TestCase` class, which provides an isolated
test environment with an in-memory database.
"""

from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import Ad, Category, User


class AdModelTest(TestCase):
    """
    Unit tests for the Ad model.

    This test suite verifies:
    - Price validation (should not allow negative prices)
    - Correct storage of valid ad prices
    """

    def setUp(self):
        """
        Set up test data for Ad model.

        This method runs before every test case, ensuring a fresh
        test environment. It creates:
        - A test category
        - A test user
        """
        self.category = Category.objects.create(name='Test Category')
        self.user = User.objects.create(username='testuser',
                                        email='test@example.com')

    def test_price_validation(self):
        """
        Ensure that an Ad cannot be created with a negative price.

        This test verifies that a `ValidationError` is raised when
        trying to save an ad with a negative price.
        """
        advertisement = Ad(
            title='Test Ad',
            description='Description',
            price=-10,  # Invalid price
            user=self.user,
            category=self.category
        )

        with self.assertRaises(ValidationError):
            advertisement.clean()  # Manually trigger model validation

    def test_valid_price(self):
        """
        Ensure that an Ad with a valid price is correctly stored.

        This test creates an ad with a valid price and verifies
        that the stored price matches the input value.
        """
        advertisement = Ad.objects.create(
            title='Test Ad',
            description='Description',
            price=10,  # Valid price
            user=self.user,
            category=self.category
        )
        self.assertEqual(advertisement.price, 10)


class SignalTest(TestCase):
    """
    Unit tests for Django signals related to the Ad model.

    This test suite verifies:
    - Automatic deactivation of ads that are older than 30 days
    """

    def test_ad_deactivation_after_30_days(self):
        """
        Ensure ads older than 30 days are automatically deactivated.

        This test creates an ad with a timestamp set to 50 days ago
        and manually triggers the expiration check. After running
        `check_expiration()`, the ad should be marked as inactive.
        """
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name='Test Category')

        # Create an ad with a created_at date 50 days in the past
        created_at = timezone.now() - timedelta(days=50)
        advertisement = Ad.objects.create(
            title='Old Ad',
            description='Description',
            price=10,
            user=user,
            category=category,
            created_at=created_at
        )

        # Ensure the timestamp is set correctly
        advertisement.created_at = created_at
        advertisement.save()

        # Trigger the expiration check
        advertisement.check_expiration()
        advertisement.refresh_from_db()

        # Verify that the ad is now inactive
        self.assertFalse(advertisement.is_active)
