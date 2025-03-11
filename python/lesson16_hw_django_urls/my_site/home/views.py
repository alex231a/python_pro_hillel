"""Module with views for handling different pages in the application."""

from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request: HttpRequest) -> HttpResponse:
    """Handles the home page request."""
    return render(request, 'home/home.html')


def about(request: HttpRequest) -> HttpResponse:
    """Handles the about page request."""
    return render(request, 'home/about.html')


def contact(request: HttpRequest) -> HttpResponse:
    """Handles the contact page request."""
    return render(request, 'home/contact.html')


def post_view(request: HttpRequest, id: Optional[int] = None) -> HttpResponse:
    """
    Handles post page requests.

    - If `POST`, redirects to the specified post ID.
    - If `GET`, renders the post page with an optional ID.
    """
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        if post_id and post_id.isdigit():
            return redirect(reverse('post', args=[post_id]))
        return render(request, 'home/post.html', {'error': 'Enter a valid ID'})

    return render(request, 'home/post.html', {'id': id})


def profile_view(request: HttpRequest,
                 username: Optional[str] = None) -> HttpResponse:
    """
    Handles profile page requests.

    - If `POST`, redirects to the specified username.
    - If `GET`, renders the profile page with an optional username.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            return redirect(reverse('profile', args=[username]))
        return render(request, 'home/profile.html',
                      {'error': "Enter a username"})

    return render(request, 'home/profile.html', {'username': username})


def event_view(
        request: HttpRequest,
        year: Optional[int] = None,
        month: Optional[int] = None,
        day: Optional[int] = None
) -> HttpResponse:
    """
    Handles event page requests.

    - If `POST`, redirects to the specified event date.
    - If `GET`, renders the event page with an optional date.
    """
    if request.method == 'POST':
        year = request.POST.get('year')
        month = request.POST.get('month')
        day = request.POST.get('day')

        if all([year, month,
                day]) and year.isdigit() and month.isdigit() and day.isdigit():
            return redirect(reverse('event', args=[year, month, day]))

        return render(request, 'home/event.html',
                      {'error': "Enter a valid year, month, and day"})

    date = {"year": year, "month": month, "day": day} if all(
        [year, month, day]) else None
    return render(request, 'home/event.html', {"date": date})
