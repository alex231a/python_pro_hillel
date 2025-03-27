"""Module that represents forms for registration and loging"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class RegisterForm(UserCreationForm):
    """
    A form for creating a new user. This form extends the default
    UserCreationForm
    and is customized for the CustomUser model.

    It includes fields for username, email, and password, with specific form
    widgets
    for improved styling and UX.
    """
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'})
    )
    """
    The username field allows the user to enter their desired username.
    It is required and uses a TextInput widget with custom CSS class for 
    styling.
    Autocomplete is disabled for security reasons.
    """

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'})
    )
    """
    The email field requires a valid email address. It uses an EmailInput 
    widget 
    and is also required for the user to complete the registration.
    Autocomplete is disabled for security reasons.
    """

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'new-password'})
    )
    """
    The first password field. It requires the user to enter a password, 
    which will be validated against the second password field. 
    The PasswordInput widget is used for secure entry, and autocomplete is 
    disabled.
    """

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'new-password'})
    )
    """
    The second password field for password confirmation. 
    It ensures the user entered the same password in both fields.
    Similar to password1, it uses a PasswordInput widget with autocomplete 
    disabled.
    """

    class Meta: # pylint: disable=too-few-public-methods
        """Class Meta"""
        model = CustomUser
        """
        The form is bound to the CustomUser model, ensuring that the form 
        fields 
        are aligned with the model's fields.
        """
        fields = ["username", "email", "password1", "password2"]
        """
        The fields included in the form. In this case, the form captures 
        the username, email, and password fields from the CustomUser model.
        """


class LoginForm(AuthenticationForm):
    """
    A form for user authentication (login). This form extends the default
    AuthenticationForm
    and provides customized form fields with custom widgets for styling.
    """
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'})
    )
    """
    The username field for logging in. It is required and uses a TextInput 
    widget 
    with custom CSS class for styling. Autocomplete is disabled for security.
    """

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'autocomplete': 'off'})
    )
    """
    The password field for logging in. It is required and uses a 
    PasswordInput widget 
    to securely enter the password. Autocomplete is disabled to ensure 
    security.
    """
