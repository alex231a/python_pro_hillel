"""Module for configuring the Django application.

This module contains the configuration for the 'board' app.
It is responsible for setting up application-specific settings and
ensuring that necessary components (such as signals) are imported
when the app is ready.
"""

import importlib

from django.apps import AppConfig


class BoardConfig(AppConfig):
    """
    Configuration class for the 'board' application.

    This class sets the default behavior of the app, such as
    automatic primary key field generation and signal registration.

    Attributes:
        default_auto_field (str): Specifies the default type of primary key
        field
            for models that do not define one explicitly.
        name (str): The name of the application within the Django project.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

    def ready(self):
        """
        Called when the application is ready.

        This method ensures that signal handlers from the 'signals' module
        are imported when the Django application starts, allowing model
        event listeners to function properly.

        Signals are used to trigger specific actions when database events
        occur,
        such as creating, updating, or deleting instances of models.

        Example:
            - Automatically creating a UserProfile when a new User is
            registered.
            - Sending notifications when a new Ad is posted.
        """
        importlib.import_module('board.signals')
