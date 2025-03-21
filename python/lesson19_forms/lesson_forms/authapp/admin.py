"""Admin module, configuring Django Admin for the advertisement system."""

from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for UserProfile model.

    Displays additional user information in the admin panel.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """

    list_display = ('user', 'bio', 'birth_date', 'location', 'avatar')
