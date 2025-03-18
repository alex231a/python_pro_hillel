"""Admin module, configuring Django Admin for the advertisement system."""

from django.contrib import admin

from .models import UserProfile, Category, Ad, Comment


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for UserProfile model.

    Displays additional user information in the admin panel.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """

    list_display = ('user', 'phone_number', 'address')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Category model.

    Allows managing advertisement categories, displaying active ad count.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """

    list_display = ('name', 'active_ads_count')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Ad model.

    Enables management of advertisements, filtering, and bulk actions.

    Attributes:
        list_display (tuple): Specifies which fields are displayed in the
        admin list view.
        list_filter (tuple): Adds filtering options in the admin panel.
        actions (list): Defines available bulk actions.
    """

    list_display = (
        'title', 'price', 'is_active', 'created_at', 'updated_at', 'category',
        'user')
    list_filter = ('is_active', 'category', 'user')
    actions = ['deactivate_expired_ads']

    def deactivate_expired_ads(self, request, queryset):
        """
        Bulk action to deactivate expired advertisements.

        Iterates over the selected ads and calls `check_expiration()`,
        ensuring expired ads are marked as inactive.

        Args:
            request (HttpRequest): The request object from Django admin.
            queryset (QuerySet): A queryset of selected advertisements.
        """
        for advertisement in queryset:
            advertisement.check_expiration()

    deactivate_expired_ads.short_description = "Deactivate expired ads"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Comment model.

    Allows managing comments on advertisements.

    Attributes:
        list_display (tuple): Fields displayed in the admin list view.
    """

    list_display = ('content', 'user', 'ad', 'created_at')
