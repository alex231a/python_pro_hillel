"""
URL configuration for the shop_api app.

This module uses Django REST Framework's DefaultRouter to automatically
generate URL patterns for the ProductViewSet.

Endpoints:
    /products/          - List all products or create a new one (GET, POST)
    /products/{id}/     - Retrieve, update, or delete a specific product (GET, PUT, DELETE)
"""

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
