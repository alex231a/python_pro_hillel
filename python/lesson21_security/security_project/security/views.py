"""Module that represents views for main requests"""

from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.signed_cookies import SessionStore
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django_ratelimit.decorators import ratelimit

from .forms import RegisterForm, LoginForm


@ratelimit(key='ip', rate='3/m', method='POST', block=True)
@csrf_protect
def register_view(request):
    """
    View to handle user registration. It displays a registration form, and
    if the form is valid, the user is created, logged in, and redirected to
    the homepage.

    - The `@ratelimit` decorator limits the number of POST requests to 3 per
    minute per IP address.
    - The `@csrf_protect` decorator ensures that CSRF protection is applied
    to the view.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the registration form or redirects to the
        homepage after successful registration.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save the new user and log them in
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'security/register.html', {'form': form})


@ratelimit(key='ip', rate='5/m', method='POST', block=True)
@csrf_protect
def login_view(request):
    """
    View to handle user login. If the login form is valid, the user is
    logged in and redirected to the homepage.

    - The `@ratelimit` decorator limits the number of POST requests to 5 per
    minute per IP address.
    - The `@csrf_protect` decorator ensures that CSRF protection is applied
    to the view.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the login form or redirects to the homepage
        after successful login.
    """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Authenticate and log the user in
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'security/login.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    """
    View to log out the user. This will log the user out and redirect them
    to the login page.

    The `@login_required` decorator ensures that the user must be logged in
    to access this view.
    If they are not logged in, they are redirected to the login page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect: Redirects to the login page after logging out.
    """
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_view(request):
    """
    Home view for logged-in users. This page is accessible only to
    authenticated users.

    The `@login_required` decorator ensures that only logged-in users can
    access this view.
    If the user is not logged in, they are redirected to the login page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the main page for logged-in users.
    """
    return render(request, 'security/main_page.html')


def error_view(request):
    """
    A test view that raises an exception to simulate a 500 error for testing
    purposes.

    This view can be used to test error handling and logging of 500 server
    errors.

    Args:
        request (HttpRequest): The request object.

    Returns:
        None: Raises an exception to simulate a server error.
    """
    # pylint: disable=broad-exception-raised
    raise Exception("Test ERROR 500")


def set_custom_session(request):
    """
    View to manually set a custom session for the user. The session stores
    the user's ID
    and is saved as a signed cookie in the user's browser.

    This can be useful for testing or custom session management logic.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: A response indicating that the session was set,
        with the session key
                      stored in a cookie.
    """
    session = SessionStore()
    session["user_id"] = request.user.id
    session.create()
    response = HttpResponse("Session set")
    # Set the session key as a cookie
    response.set_cookie(settings.SESSION_COOKIE_NAME, session.session_key)
    return response
