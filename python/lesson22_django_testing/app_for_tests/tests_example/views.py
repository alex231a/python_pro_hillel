"""
This module defines views for managing tasks in a Django application.

It includes both function-based views (FBVs) and class-based views (CBVs)
for handling tasks:

Function-Based Views:
- `add_todo_view`: Handles task creation via a form.
- `show_todo_view`: Displays all tasks.
- `delete_todo_view`: Deletes a specified task with error handling.

Class-Based Views:
- `TodoListView`: API endpoint for retrieving a list of tasks.

The views support both HTML templates and REST API responses for flexibility.
"""

from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics

from .forms import TaskForm
from .models import Tasks
from .serializers import TaskSerializer


def add_todo_view(request):
    """
    Handles task creation through a form submission.

    - If the request method is POST, validates and saves the task.
    - Displays a success or error message based on the validation result.
    - If the request method is GET, renders an empty form.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered template with the task form.
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been successfully added')
            return redirect('show_todo')
        messages.error(request, 'Error! Check input information')
        return render(request, 'tests_example/add_todo.html', {'form': form})

    form = TaskForm()
    return render(request, 'tests_example/add_todo.html', {'form': form})


def show_todo_view(request):
    """
    Displays a list of all tasks.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered template with a list of tasks.
    """
    # pylint: disable=no-member
    todos = Tasks.objects.all()
    return render(request, 'tests_example/todo_list.html', {'todos': todos})


def delete_todo_view(request, task_id):
    """
    Deletes a specific task by its ID.

    - If the task exists, it is deleted, and a success message is displayed.
    - Handles `IntegrityError` in case of related data issues.
    - Handles any other exceptions and provides a meaningful error message.

    Args:
        request (HttpRequest): The incoming HTTP request.
        task_id (int): The ID of the task to be deleted.

    Returns:
        HttpResponseRedirect: Redirects back to the task list page.
    """
    try:
        todo = get_object_or_404(Tasks, id=task_id)
        todo.delete()
        messages.success(request, 'Task has been successfully deleted')
    except IntegrityError:
        messages.error(request,
                       'This task could not be deleted due to related data')
    except ValueError as error:
        messages.error(request, f"Value error: {str(error)}")
    return redirect('show_todo')


class TodoListView(generics.ListAPIView):
    """
    API endpoint for retrieving a list of tasks.

    Attributes:
        queryset (QuerySet): Retrieves all tasks from the database.
        serializer_class (Serializer): Defines the serializer for task data.
    """
    # pylint: disable=no-member
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
