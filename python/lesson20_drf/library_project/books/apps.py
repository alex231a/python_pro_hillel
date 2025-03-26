"""Module containing the configuration for the 'books' application."""

from django.apps import AppConfig


class BooksConfig(AppConfig):
    """
    Configuration class for the 'books' application.

    This class defines application-specific settings such as the default
    primary key field type and the application name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
