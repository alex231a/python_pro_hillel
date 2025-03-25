"""Module with apps config"""
from django.apps import AppConfig


class BooksConfig(AppConfig):
    """Class BooksConfig"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
