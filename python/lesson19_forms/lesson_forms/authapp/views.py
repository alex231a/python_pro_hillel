"""Views for handling user authentication, registration, and profile
management."""

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, \
    update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserFormRegistration, LoginForm, UserProfileForm, \
    PasswordChangeForm
from .models import UserProfile


def main(request):
    """
    Render the main page of the application.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered main page.
    """
    return render(request, "authapp/main_page.html")


def registration(request):
    """
    Handle user registration.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered registration page with form.
    """
    if request.method == "POST":
        form = UserFormRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Registration successful! You can now log in.")
            return redirect('login')
        messages.error(request,
                       "There was an error with your registration. Please "
                       "check the form.")
        return render(request, "authapp/registration.html", {"form": form})

    form = UserFormRegistration()
    return render(request, "authapp/registration.html", {"form": form})


def login_view(request):
    """
    Handle user login.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered login page with form.
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("main_page")
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "authapp/login.html", {"form": form})


def logout_view(request):
    """
    Handle user logout.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect: Redirects to login page.
    """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


@login_required
def profile(request):
    """
    Display user profile information.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered profile page.
    """
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)  # pylint: disable=no-member
    return render(request, "authapp/profile.html",
                  {"user_profile": user_profile})


@login_required
def edit_profile(request):
    """
    Allow users to edit their profile information.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered edit profile page with form.
    """
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user) # pylint: disable=no-member
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES,
                               instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Your profile has been updated successfully.")
            return redirect("profile")

        messages.error(request,
                       "There was an error updating your profile. Please "
                       "try again.")
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, "authapp/edit_profile.html", {"form": form})


@login_required
def change_password(request):
    """
    Allow users to change their password.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered password change page with form.
    """
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,
                             "Your password has been changed successfully.")
            return redirect("profile")
        messages.error(request,
                       "There was an error changing your password. "
                       "Please try again.")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "authapp/change_password.html", {"form": form})


@login_required
def delete_account(request):
    """
    Allow users to delete their account.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect: Redirects to login page after account deletion.
    """
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.success(request,
                         "You have successfully deleted your account.")
        return redirect("login")
    return render(request, 'authapp/delete_account.html')
