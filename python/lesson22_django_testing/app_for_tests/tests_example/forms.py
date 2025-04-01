"""Module with forms"""

import datetime

from django import forms

from .models import Tasks


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating tasks.

    This form is based on the `Tasks` model and provides fields for:
    - `title`: A short text input for the task title.
    - `description`: A textarea for task details.
    - `due_date`: A date field with validation to prevent past dates.
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta class for TaskForm."""
        model = Tasks
        fields = ('title', 'description', 'due_date')
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter task title'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter task description', 'rows': 3,
                       'cols': 40}),
        }

    def clean_due_date(self):
        """
        Custom validation for the `due_date` field.

        Ensures that the due date is not set in the past. If the user
        provides a past date, a validation error is raised.

        Returns:
            datetime.date: The validated due date.

        Raises:
            forms.ValidationError: If the due date is before today.
        """
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < datetime.date.today():
            raise forms.ValidationError('Due date cannot be before today')
        return due_date
