from django.contrib import admin
from books.models import Book, Author, Tag

class BookAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "created", "created", "author_id"]
   list_filter = ["title"]
   search_fields = ["title", "author_id"]


admin.site.register(Book, BookAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   list_display = ['id', 'word']
