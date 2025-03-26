"""Module defining URL routes for the books application."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include all routes from the router
]
