from rest_framework import serializers

from books.models import Book, Author, Tag

class BookSerializer(serializers.ModelSerializer):
   class Meta:
       model = Book
       fields = ('id', 'title', 'created', 'author_id', 'image', 'tags')

class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ('id', 'name')

class TagSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tag
       fields = ('id', 'word', 'created')
