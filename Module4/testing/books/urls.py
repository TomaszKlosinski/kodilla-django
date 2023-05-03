from django.urls import path
from django.views.generic import ListView
from books.models import Book, Author
from books.views import books_list, book_details, authors_list, author_details, borrows_list

app_name = "books"

urlpatterns = [
   path('', books_list, name="list"),
   path('<int:id>', book_details, name="details"),
   path('authors', authors_list, name="authors"),
   path('authors/<int:id>', author_details, name="author"),
   path('borrows', borrows_list, name="borrows"),

]
