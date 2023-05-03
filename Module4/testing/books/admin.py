from django.contrib import admin
from books.models import Book, Author, Tag, Borrow

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


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'book_id', 'borrowed', 'returned', 'is_returned']
