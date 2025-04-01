"""
This module defines the `Tasks` model for managing task-related data.

The `Tasks` model includes:
- `title`: A unique title for the task.
- `description`: An optional text description.
- `due_date`: A date field with a default value set to 10 days from today.

The `get_default_date` function ensures that new tasks have a default due date
set to 10 days in the future.
"""

import datetime

from django.db import models


def get_default_date():
    """
    Returns the default due date for tasks, which is 10 days from today.

    Returns:
        datetime.date: The default due date.
    """
    return datetime.date.today() + datetime.timedelta(days=10)


class Tasks(models.Model):
    """
    Represents a task entity with a title, optional description, and a due
    date.

    Attributes:
        title (CharField): A unique title for the task (max length 75
        characters).
        description (TextField): An optional description of the task.
        due_date (DateField): The date by which the task should be completed,
                              defaults to 10 days from creation.
    """
    title = models.CharField(
        max_length=75,
        unique=True,
        help_text="Type title"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Type description or leave empty"
    )
    due_date = models.DateField(default=get_default_date)

    def __str__(self):
        """
        Returns a string representation of the task, which is its title.

        Returns:
            str: The task title.
        """
        return str(self.title)
