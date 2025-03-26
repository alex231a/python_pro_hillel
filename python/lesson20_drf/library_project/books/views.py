"""Module containing view sets for the Book API."""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    Pagination class that defines standard pagination settings.
    - Default page size: 10
    - Allows customization via 'page_size' query parameter
    - Maximum allowed page size: 100
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    ViewSet for managing books in the API.
    - Requires authentication (JWT or Token)
    - Supports filtering, searching, and ordering
    - Implements pagination with a default page size of 10
    """
    queryset = Book.objects.all()   # pylint: disable=no-member
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_fields = ['author', 'genre',
                        'publication_year']  # Filtering options
    search_fields = ['title']  # Enables searching by book title
    ordering_fields = ['publication_year',
                       'title']  # Allows sorting by title or publication year
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        """
        Override the default create method to associate the book with the
        authenticated user.
        """
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """
        Override the delete method to restrict book deletion to admin users
        only.
        """
        if not request.user.is_staff:
            return Response({'error': 'Only admins can delete books'},
                            status=403)
        return super().destroy(request, *args, **kwargs)
