"""Module containing views for the board application.

This module includes:
- `BoardView`: A class-based view that handles displaying ads with filters and sorting.
- `admin_statistics`: A function-based view that generates statistics for administrators.
"""

from django.db.models import Count
from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.views import View

from .models import Ad, Category, UserProfile, Comment


class BoardView(View):
    """
    View for displaying a list of advertisements with filtering and sorting options.

    **Filters:**
    - `category`: Filter ads by category.
    - `user`: Filter ads by user.
    - `price_min`: Minimum price filter.
    - `price_max`: Maximum price filter.
    - `search`: Search ads by title.
    - `filter`: Special filters:
        - `last_month`: Ads created in the last 30 days.
        - `active_category`: Only active ads within a selected category.
        - `comment_count`: Sort ads by the number of comments.
        - `user_ads`: Filter ads by a specific user.

    **Sorting Options:**
    - `price_asc`: Sort by price (ascending).
    - `price_desc`: Sort by price (descending).
    - `created_at_asc`: Sort by creation date (oldest first).
    - `created_at_desc`: Sort by creation date (newest first).

    **Template:**
    - Renders `board/board.html` with filtered ads and categories.
    """

    def get(self, request):
        """
        Handles GET requests to display ads with filters and sorting.

        Args:
            request (HttpRequest): The incoming request object.

        Returns:
            HttpResponse: Rendered template with ads and filtering options.
        """
        filter_type = request.GET.get('filter')
        selected_category = request.GET.get('category')
        selected_user = request.GET.get('user')
        search_query = request.GET.get('search', '')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        sort_by = request.GET.get('sort', 'created_at_desc')

        # Retrieve all ads (queryset)
        queryset = Ad.objects.all()

        # Apply filters
        if selected_category:
            queryset = queryset.filter(category_id=selected_category)
        if selected_user:
            queryset = queryset.filter(user_id=selected_user)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        # Special filters
        if filter_type == 'last_month':
            queryset = queryset.filter(
                created_at__gte=now() - timedelta(days=30))
        elif filter_type == 'active_category':
            queryset = queryset.filter(is_active=True)
            if selected_category:
                queryset = queryset.filter(category_id=selected_category)
        elif filter_type == 'comment_count':
            queryset = queryset.annotate(
                comment_count=Count('comments')).order_by('-comment_count')
        elif filter_type == "user_ads":
            user_id = request.GET.get('user', 1)
            queryset = queryset.filter(user_id=user_id)

        # Sorting options
        sorting_options = {
            'price_asc': 'price',
            'price_desc': '-price',
            'created_at_asc': 'created_at',
            'created_at_desc': '-created_at'
        }
        queryset = queryset.order_by(
            sorting_options.get(sort_by, '-created_at'))

        # Count comments for each ad
        queryset = queryset.annotate(comment_count=Count('comments'))

        # Retrieve all categories and user profiles
        categories = Category.objects.all()
        user_profiles = UserProfile.objects.all()

        return render(request, "board/board.html", {
            "ads": queryset,
            "categories": categories,
            "user_profiles": user_profiles,
            "selected_category": selected_category,
            "selected_user": selected_user,
            "search_query": search_query,
            "sort_by": sort_by,
            "price_min": price_min,
            "price_max": price_max,
        })


def admin_statistics(request):
    """
    View for displaying statistical data about advertisements.

    **Statistics:**
    - `total_ads`: Total number of ads in the system.
    - `active_ads`: Number of currently active ads.
    - `inactive_ads`: Number of inactive ads.
    - `total_comments`: Total number of comments on all ads.
    - `ads_per_category`: Number of ads in each category.

    **Template:**
    - Renders `board/statistics.html` with the statistics.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: Rendered template with admin statistics.
    """
    total_ads = Ad.objects.count()
    active_ads = Ad.objects.filter(is_active=True).count()
    inactive_ads = Ad.objects.filter(is_active=False).count()
    total_comments = Comment.objects.count()
    ads_per_category = Category.objects.annotate(ad_count=Count('ads'))

    context = {
        "total_ads": total_ads,
        "active_ads": active_ads,
        "inactive_ads": inactive_ads,
        "total_comments": total_comments,
        "ads_per_category": ads_per_category,
    }

    return render(request, "board/statistics.html", context)
