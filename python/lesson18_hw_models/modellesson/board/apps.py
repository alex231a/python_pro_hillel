"""Module for apps"""
import importlib

from django.apps import AppConfig


class BoardConfig(AppConfig):
    """Config for app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

    def ready(self):
        """Function called when app is ready"""
        importlib.import_module('board.signals')
