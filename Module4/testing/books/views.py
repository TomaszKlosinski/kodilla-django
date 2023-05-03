from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator

from books.models import Book, Author, Borrow

from datetime import datetime


def books_list(request):
   books = Book.objects.all()

   paginator = Paginator(books, 3)
   page_number = request.GET.get('page')
   books = paginator.get_page(page_number)

   return render(
       request=request,
       template_name="books/books_list.html",
       context={"books": books}
   )


def book_details(request, id):
   book = Book.objects.get(id=id)
   borrows = Borrow.objects.filter(book_id=book)

   if request.method == "POST":
       user = request.user
       Borrow.objects.create(user=user, book_id=book)


   borrowable = True
   if borrows:
       for b in borrows:
           if not b.is_returned:
               borrowable = False

   return render(
       request=request,
       template_name="books/book_details.html",
       context={"book": book, "borrowable": borrowable}
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
   author_books = Book.objects.filter(author_id=author.id)
   return render(
       request=request,
       template_name="books/author_details.html",
       context={"author": author, "author_books": author_books}
   )


def borrows_list(request):
   if request.method == 'POST' and 'borrow_id' in request.POST:
       borrow = Borrow.objects.get(id=request.POST['borrow_id'])
       borrow.is_returned = True
       borrow.returned = datetime.now()
       borrow.save()


   borrows = Borrow.objects.filter(is_returned=False)
   return render(
       request=request,
       template_name="books/borrows_list.html",
       context={"borrows": borrows}
   )
