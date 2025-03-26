"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

# API documentation schema
schema_view = get_schema_view(  # pylint: disable=invalid-name
    openapi.Info(
        title="Library API",
        default_version="v1",
        description="API for managing a book library",
    ),
    public=True,
    permission_classes=[AllowAny],
)

# URL patterns for the project
urlpatterns = [
    path("admin/", admin.site.urls),  # Django admin panel
    path("api/", include("books.urls")),  # Book management API endpoints

    # JWT Authentication endpoints
    path("api/token/", TokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(),
         name="token_refresh"),

    # API documentation
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
]
