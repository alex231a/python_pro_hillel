"""Module with test cases"""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class BookAPITestCase(APITestCase):
    """
    Test case for the Book API endpoints.
    Ensures that CRUD operations, filtering, searching, and pagination work
    correctly.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test user and
        authenticating the client.
        """
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        self.client.force_authenticate(user=self.user)

    def test_create_book(self):
        """
        Test creating a new book.
        Expects a 201 Created response.
        """
        data = {
            'title': 'New Book',
            'author': 'John Doe',
            'genre': 'Fiction',
            'publication_year': 2022,
            'user': self.user.id
        }
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books(self):
        """
        Test retrieving the list of books.
        Expects a 200 OK response.
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_books(self):
        """
        Test filtering books by author.
        Expects a 200 OK response.
        """
        response = self.client.get('/api/books/?author=John Doe')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        """
        Test searching books by title.
        Expects a 200 OK response.
        """
        response = self.client.get('/api/books/?search=New')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pagination(self):
        """
        Test pagination of books (page 1).
        Expects a 200 OK response.
        """
        response = self.client.get('/api/books/?page=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
