"""Module for apps"""

from django.apps import AppConfig


class SecurityConfig(AppConfig):
    """
    Configuration class for the 'security' application in a Django project.

    This class is responsible for defining application-specific settings,
    such as
    the default auto field type and the application name.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    """
    Specifies the type of auto-incrementing primary key field to use by default
    for models in this application. 'BigAutoField' ensures compatibility 
    with large datasets.
    """

    name = 'security'
    """
    Defines the name of the application, which corresponds to the directory
    structure in the Django project.
    """
