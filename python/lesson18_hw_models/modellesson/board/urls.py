"""Module for urls"""

from django.urls import path

from .views import BoardView, admin_statistics

urlpatterns = [
    path('', BoardView.as_view(), name='board'),
    path('statistics/', admin_statistics, name='admin_statistics'),
]
