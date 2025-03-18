"""Module Views"""

from django.db.models import Count
from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.views import View

from .models import Ad, Category, UserProfile, Comment


# Create your views here.
class BoardView(View):
    """Class BoardViews"""

    def get(self, request):
        """Method for handling GET requests"""
        filter_type = request.GET.get('filter')
        selected_category = request.GET.get('category')
        selected_user = request.GET.get('user')
        search_query = request.GET.get('search', '')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        sort_by = request.GET.get('sort', 'created_at_desc')

        ads = Ad.objects.all()  # pylint: disable=no-member

        if selected_category:
            ads = ads.filter(category_id=selected_category)

        if selected_user:
            ads = ads.filter(user_id=selected_user)

        if price_min:
            ads = ads.filter(price__gte=price_min)

        if price_max:
            ads = ads.filter(price__lte=price_max)

        if search_query:
            ads = ads.filter(title__icontains=search_query)

        if filter_type == 'last_month':
            ads = ads.filter(created_at__gte=now() - timedelta(days=30))

        elif filter_type == 'active_category':
            if selected_category:
                ads = ads.filter(category_id=selected_category, is_active=True)
            else:
                ads = ads.filter(is_active=True)

        elif filter_type == 'comment_count':
            ads = ads.annotate(comment_count=Count('comments')).order_by(
                '-comment_count')

        elif filter_type == "user_ads":
            user_id = request.GET.get('user', 1)
            ads = ads.filter(user_id=user_id)

        sorting_options = {
            'price_asc': 'price',
            'price_desc': '-price',
            'created_at_asc': 'created_at',
            'created_at_desc': '-created_at'
        }
        ads = ads.order_by(sorting_options.get(sort_by, '-created_at'))

        ads = ads.annotate(comment_count=Count('comments'))

        categories = Category.objects.all()  # pylint: disable=no-member
        user_profiles = UserProfile.objects.all()  # pylint: disable=no-member

        return render(request, "board/board.html", {
            "ads": ads,
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
    """Function handle requests for admin statistics"""

    total_ads = Ad.objects.count()  # pylint: disable=no-member
    active_ads = Ad.objects.filter(is_active=True).count()  # pylint: disable=no-member
    inactive_ads = Ad.objects.filter(is_active=False).count()  # pylint: disable=no-member
    total_comments = Comment.objects.count()  # pylint: disable=no-member
    ads_per_category = Category.objects.annotate(ad_count=Count('ads'))  # pylint: disable=no-member

    context = {
        "total_ads": total_ads,
        "active_ads": active_ads,
        "inactive_ads": inactive_ads,
        "total_comments": total_comments,
        "ads_per_category": ads_per_category,
    }

    return render(request, "board/statistics.html", context)
