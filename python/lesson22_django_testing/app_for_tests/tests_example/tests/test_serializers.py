"""
Unit tests for the TaskSerializer in Django REST framework.

This module contains tests to validate the TaskSerializer, ensuring correct
serialization and deserialization of task data, as well as enforcing
validation rules.

Test Cases:
- `test_valid_serializer`: Ensures that valid data is correctly serialized.
- `test_invalid_serializer_missing_title`: Verifies that missing required
fields cause validation failure.
- `test_invalid_serializer_past_due_date`: Checks that a task with a past
due date is rejected.

Fixtures:
- `valid_task_data`: Provides valid task data.
- `invalid_task_data`: Provides task data with a missing required field (
title).
- `past_due_date_data`: Provides task data with a past due date to test
validation.

Logging:
Each test logs its start to aid in debugging.
"""

import inspect
import logging
from datetime import date, timedelta

import pytest

from tests_example.serializers import TaskSerializer

logger = logging.getLogger(__name__)


class TestTaskSerializer:
    """
    Test suite for the TaskSerializer.
    """

    @pytest.fixture
    def valid_task_data(self):
        """
        Fixture providing valid task data.
        """
        return {
            'title': 'Task for serialization',
            'description': 'Test task description',
            'due_date': date.today() + timedelta(days=5)
        }

    @pytest.fixture
    def invalid_task_data(self):
        """
        Fixture providing invalid task data with a missing title field.
        """
        return {
            'description': 'Missing title field',
            'due_date': date.today() + timedelta(days=5)
        }

    @pytest.fixture
    def past_due_date_data(self):
        """
        Fixture providing task data with a due date in the past.
        """
        return {
            'title': 'Past Date Task',
            'description': 'Task with past due date',
            'due_date': date.today() - timedelta(days=5)
        }

    @pytest.mark.django_db
    def test_valid_serializer(self, valid_task_data):
        """
        Positive test: Ensure TaskSerializer validates correct task data.
        """
        logger.info("Started test %s", inspect.currentframe().f_code.co_name)
        serializer = TaskSerializer(data=valid_task_data)
        assert serializer.is_valid(), serializer.errors

    @pytest.mark.django_db
    def test_invalid_serializer_missing_title(self, invalid_task_data):
        """
        Negative test: Ensure TaskSerializer fails when the title field is
        missing.
        """
        logger.info("Started test %s", inspect.currentframe().f_code.co_name)
        serializer = TaskSerializer(data=invalid_task_data)
        assert not serializer.is_valid()
        assert 'title' in serializer.errors

    @pytest.mark.django_db
    def test_invalid_serializer_past_due_date(self, past_due_date_data):
        """
        Negative test: Ensure TaskSerializer rejects a past due date.
        """
        logger.info("Started test %s", inspect.currentframe().f_code.co_name)
        serializer = TaskSerializer(data=past_due_date_data)
        assert not serializer.is_valid()
        assert 'due_date' in serializer.errors
