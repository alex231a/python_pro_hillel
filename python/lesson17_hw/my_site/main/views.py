"""Module with views for handling different pages in the application."""

import json
from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


def home(request: HttpRequest) -> HttpResponse:
    """Handles the home page request."""
    context = {"last_updated": datetime.now()}
    return render(request, 'main/home.html', context)


def about(request: HttpRequest) -> HttpResponse:
    """Handles the about page request."""
    context = {"last_updated": datetime.now()}
    return render(request, 'main/about.html', context)


class ContactView(View):
    """Class Contact view."""

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        """Handles the contact page request."""
        context = {"last_updated": datetime.now()}
        return render(request, 'main/contact.html', context)


class ServiceView(View):
    """Class Service view."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Handles the service page get requests."""
        with open("main/data/services.json", "r", encoding="utf-8") as file:
            services_list = json.load(file)
        context = {"services": services_list, "last_updated": datetime.now()}
        return render(request, 'main/services.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        """Handles the service page post requests."""

        query = request.POST.get('query', '').strip().lower()

        with open("main/data/services.json", "r", encoding="utf-8") as file:
            services_list = json.load(file)
        services_output_list = [service for service in services_list if
                                query in service["name"].lower()]
        context = {
            "services": services_output_list,
            "last_updated": datetime.now()
        }

        return render(request, 'main/services.html', context)
