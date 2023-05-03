from rest_framework.viewsets import ModelViewSet

from books.models import Book, Author
from books.serializers import BookSerializer, AuthorSerializer

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
