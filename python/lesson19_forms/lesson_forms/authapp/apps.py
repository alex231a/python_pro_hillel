"""Module with apps.py"""
import importlib

from django.apps import AppConfig


class AuthConfig(AppConfig):
    """Configure auth app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authapp'

    def ready(self):
        """Method called when auth app is loaded."""
        importlib.import_module('authapp.signals')
