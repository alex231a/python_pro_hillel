"""Tests for some functionalities"""
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import Ad, Category, User


class AdModelTest(TestCase):
    """Class AdModelTest"""

    def setUp(self):
        """Setup"""
        self.category = Category.objects.create( # pylint: disable=no-member
            name='Test Category')  # pylint: disable=no-member
        self.user = User.objects.create(username='testuser',
                                        email='test@example.com')

    def test_price_validation(self):
        """Test price validation"""
        advertisement = Ad(title='Test Ad', description='Description',
                           price=-10, user=self.user,
                           category=self.category)  # pylint: disable=no-member
        with self.assertRaises(ValidationError):
            advertisement.clean()

    def test_valid_price(self):
        """Test valid price"""
        advertisement = Ad.objects.create(title='Test Ad', # pylint: disable=no-member
                                          description='Description',
                                          # pylint: disable=no-member
                                          price=10, user=self.user,
                                          category=self.category)  # pylint:
        # disable=no-member
        self.assertEqual(advertisement.price, 10)


class SignalTest(TestCase):
    """Class SignalTest"""

    def test_ad_deactivation_after_30_days(self):
        """Method ad_deactivation_after_30_days"""
        user = User.objects.create(username='testuser')
        category = Category.objects.create( # pylint: disable=no-member
            name='Test Category')  # pylint: disable=no-member
        created_at = timezone.now() - timedelta(days=50)
        advertisment = Ad.objects.create(title='Old Ad', # pylint: disable=no-member
                                         description='Description',
                                         # pylint: disable=no-member
                                         price=10, user=user,
                                         category=category,
                                         # pylint: disable=no-member
                                         created_at=created_at)
        advertisment.created_at = timezone.now() - timedelta(days=50)
        advertisment.save()
        advertisment.check_expiration()
        advertisment.refresh_from_db()
        self.assertFalse(advertisment.is_active)
