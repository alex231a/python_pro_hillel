"""
Unit tests for the To-Do form submission in Django.

This module tests the `add_todo` view to ensure correct form handling
and validation. It includes both positive and negative test cases.

Test Cases:
- `test_add_todo_view`: Ensures a valid task can be successfully added.
- `test_add_todo_view_wo_title`: Checks that a task without a title is
rejected.
- `test_add_todo_view_with_date_in_past`: Ensures a task with a past due
date is rejected.

Fixtures:
- `setup_method`: Initializes the test client, form URLs, and different test
datasets.

Logging:
- Each test logs its start and the response status code for better debugging.
"""

import datetime
import logging

import pytest
from django.test import Client
from django.urls import reverse

from tests_example.models import Tasks

logger = logging.getLogger(__name__)


class TestToDoForm:
    """
    Test suite for the To-Do form submission.
    """

    # pylint: disable=attribute-defined-outside-init
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """
        Fixture to set up test client and test data before each test.
        """
        self.client = Client()
        self.url = reverse('add_todo')
        self.valid_data = {
            'title': 'New Task',
            'description': 'This is a new task.',
            'due_date': datetime.date.today() + datetime.timedelta(days=10)
        }
        self.data_wo_title = {
            'description': 'This is a task without title.',
            'due_date': datetime.date.today() + datetime.timedelta(days=10)
        }
        self.data_with_date_in_past = {
            'title': 'New Task',
            'description': 'This is a new task.',
            'due_date': datetime.date.today() - datetime.timedelta(days=10)
        }
        logger.info("Setup method initialized with test data.")

    @pytest.mark.django_db
    def test_add_todo_view(self):
        """
        Positive test: Ensure valid task data is processed correctly.
        """
        logger.info("Started test_add_todo_view")
        response = self.client.post(self.url, self.valid_data)
        logger.info("Response status code: %s", response.status_code)
        assert response.status_code == 302
        assert Tasks.objects.filter(
            title='New Task').exists()  # pylint: disable=no-member

    @pytest.mark.django_db
    def test_add_todo_view_wo_title(self):
        """
        Negative test: Ensure a task without a title is rejected.
        """
        logger.info("Started test_add_todo_view_wo_title")
        response = self.client.post(self.url, self.data_wo_title)
        logger.info("Response status code: %s", response.status_code)
        assert response.status_code == 200
        assert b'Error! Check input information' in response.content
        assert not Tasks.objects.filter(  # pylint: disable=no-member
            description='This is a task without title.').exists()

    @pytest.mark.django_db
    def test_add_todo_view_with_date_in_past(self):
        """
        Negative test: Ensure a task with a past due date is rejected.
        """
        logger.info("Started test_add_todo_view_with_date_in_past")
        response = self.client.post(self.url, self.data_with_date_in_past)
        logger.info("Response status code: %s", response.status_code)
        assert response.status_code == 200
        assert b'Error! Check input information' in response.content
        assert not Tasks.objects.filter(  # pylint: disable=no-member
            description='This is a new task.').exists()
