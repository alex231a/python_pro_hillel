"""Module with forms"""

from django import forms
from django.contrib.auth.forms import \
    PasswordChangeForm as BasePasswordChangeForm
from django.core.exceptions import ValidationError

from .models import UserProfile, User


class UserFormRegistration(forms.ModelForm):
    """
    Form for user registration.
    Includes validation for unique username and email, as well as password
    confirmation.
    """
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       label="Confirm Password")

    class Meta:
        """Meta class for UserFormRegistration."""
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        """
        Custom validation to ensure passwords match and the username/email
        are unique.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match")

        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if User.objects.filter(username=username).exists():
            self.add_error('username',
                           f"User with username {username} already exists")

        if User.objects.filter(email=email).exists():
            self.add_error('email', f"User with email {email} already exists")

        return cleaned_data

    def save(self, commit=True):
        """
        Save the user instance and hash the password before storing it.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """
    Simple login form requiring username and password.
    """
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class UserProfileForm(forms.ModelForm):
    """
    Form for editing user profile information.
    Includes validation for avatar size and format.
    """
    MAX_SIZE = 2 * 1024 * 1024  # 2MB limit

    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'Format: YYYY-MM-DD'}),
        help_text="Format: YYYY-MM-DD (e.g., 2025-03-20)"
    )

    class Meta:
        """Meta class for UserProfileForm."""
        model = UserProfile
        fields = ('bio', 'birth_date', 'location', 'avatar')

    def clean_avatar(self):
        """
        Validate the uploaded avatar file, checking size and format.
        """
        avatar = self.cleaned_data.get('avatar')

        if avatar:
            if avatar.size > self.MAX_SIZE:
                raise ValidationError(
                    f"Avatar must be less than "
                    f"{self.MAX_SIZE / (1024 * 1024)} MB")

            if hasattr(avatar,
                       'content_type') and not avatar.content_type.startswith(
                "image/"):
                raise ValidationError("Only image files are allowed.")

        return avatar


class PasswordChangeForm(BasePasswordChangeForm):
    """
    Form for changing user password with validation to ensure the new
    password is different from the old one.
    """
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, user, *args, **kwargs):
        """
        Initialize the form and store the user instance.
        """
        super().__init__(user, *args, **kwargs)
        self.user = user

    def clean(self):
        """
        Ensure the new password is different from the current password.
        """
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password1 = cleaned_data.get("new_password1")

        if old_password and new_password1 and old_password == new_password1:
            raise forms.ValidationError(
                "New password must be different from the current password."
            )

        return cleaned_data
