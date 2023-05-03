from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from books.models import Book, Author


def books_list(request):
   books = Book.objects.all()
   return render(
       request=request,
       template_name="books/books_list.html",
       context={"books": books}
   )


def book_details(request, id):
   book = Book.objects.get(id=id)
   return render(
       request=request,
       template_name="books/book_details.html",
       context={"book": book}
   )


def authors_list(request):
   authors = Author.objects.all()
   return render(
       request=request,
       template_name="books/authors_list.html",
       context={"authors": authors}
   )


def author_details(request, id):
   author = Author.objects.get(id=id)
   return render(
       request=request,
       template_name="books/author_details.html",
       context={"author": author}
   )
