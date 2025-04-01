"""Module apps.py"""
from django.apps import AppConfig


class TestsExampleConfig(AppConfig):
    """
    Django application configuration for the 'tests_example' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tests_example'
