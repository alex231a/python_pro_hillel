"""
App configuration for the shop_api application.

This configuration is used by Django to initialize the REST API module,
which provides external access to the shop's resources.
"""

from django.apps import AppConfig


class ShopApiConfig(AppConfig):
    """
    Configuration class for the shop_api Django app.

    This app serves as the REST API layer for the e-commerce platform,
    exposing endpoints for products, orders, and other resources.

    Attributes:
        default_auto_field (str): Specifies the default primary key field type.
        name (str): The full Python path to the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop_api'
