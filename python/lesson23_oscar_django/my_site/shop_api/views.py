"""
ViewSet for retrieving product information via the REST API.

This module defines a read-only viewset for the Product model,
allowing clients to list and retrieve product data.
"""

from oscar.apps.catalogue.models import Product  # pylint: disable=import-error
from rest_framework import viewsets

from .serializers import ProductSerializer


# pylint: disable=too-many-ancestors
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read-only viewset for viewing Oscar products.

    This ViewSet provides `list()` and `retrieve()` actions,
    exposing essential product information to API clients.

    Attributes:
        queryset (QuerySet): All available product instances.
        serializer_class (Serializer): Serializer used for product data.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
