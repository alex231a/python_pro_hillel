"""
Serializer for Oscar's Product model.

This serializer exposes selected fields of a product
via the REST API, allowing external services to access
product information.
"""

from oscar.apps.catalogue.models import Product # pylint: disable=import-error
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """
    Serialize basic product information for API consumers.

    Fields:
        - id: Unique identifier of the product.
        - title: Product title (derived from `get_title()`).
        - description: Detailed product description.
    """

    class Meta: # pylint: disable=too-few-public-methods
        """Class meta options."""
        model = Product
        fields = ['id', 'title', 'description']
