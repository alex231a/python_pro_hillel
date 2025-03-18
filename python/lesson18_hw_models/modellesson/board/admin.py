"""Admin module, here you can include models in admin panel"""
from django.contrib import admin

from .models import UserProfile, Category, Ad, Comment


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """User profile admin class"""
    list_display = ('user', 'phone_number', 'address')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin class"""
    list_display = ('name', 'active_ads_count')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """Admin class"""
    list_display = (
        'title', 'price', 'is_active', 'created_at', 'updated_at', 'category',
        'user')
    list_filter = ('is_active', 'category', 'user')
    actions = ['deactivate_expired_ads']

    def deactivate_expired_ads(self, queryset):
        """Function to deactivate expired ads"""
        for advertisement in queryset:
            advertisement.check_expiration()

    deactivate_expired_ads.short_description = "Deactivate expired ads"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin class"""
    list_display = ('content', 'user', 'ad', 'created_at')
