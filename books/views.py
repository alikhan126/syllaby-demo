from rest_framework import viewsets


from books.models import Book, Section
from books.serializers import BookSerializer, SectionSerializer
from books.permissions import IsAuthorOrCollaborator


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user books.
    """

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthorOrCollaborator]


class SectionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user book sections.
    """

    serializer_class = SectionSerializer
    queryset = Section.objects.all()
