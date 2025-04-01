"""
Django admin configuration for the Tasks model.

This module registers the Tasks model with the Django admin interface,
allowing administrators to manage tasks through the Django admin panel.

Usage:
- Ensure that the 'Tasks' model is defined in the models.py file.
- Include this module in your Django application.
- Access the Django admin panel to manage tasks.

Example:
    Admin users can add, edit, and delete tasks through the Django admin
    interface.
"""

from django.contrib import admin

from .models import Tasks

# Register the Tasks model to make it available in the Django admin panel
admin.site.register(Tasks)
