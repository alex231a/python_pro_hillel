"""Module containing models for the Book library application."""

from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    """
    Model representing a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author's name.
        genre (str): The genre of the book.
        publication_year (int): The year the book was published.
        created_at (datetime): The timestamp when the book record was created.
        user (User): The user who added the book.

    Methods:
        __str__(): Returns the title of the book as its string representation.
    """

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the title of the book."""
        return str(self.title)
