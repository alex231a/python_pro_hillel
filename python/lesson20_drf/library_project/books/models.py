"""Module with models for Book library"""
from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    """Class model for Book library"""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return book title"""
        return self.title
