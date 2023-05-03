from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from posts.models import Post, Author
from posts.forms import AuthorForm, PostForm

def index(request):
    c = {"title": "Welcome to blog posts app."}
    return render(
        request=request,
        template_name="posts/home.html",
        context=c
    )


def posts_list(request):
   posts = Post.objects.all()
   form = PostForm()
   if request.method == "POST":
       form = PostForm(data=request.POST, files=request.FILES)
       if form.is_valid():
           form.save()
           messages.add_message(
               request,
               messages.SUCCESS,
               "New post added"
           )

   return render(
       request=request,
       template_name="posts/posts_list.html",
       context={"posts": posts, "form": form}
   )


def post_details(request, id):
   post = Post.objects.get(id=id)
   return render(
       request=request,
       template_name="posts/post_details.html",
       context={"post": post}
   )


def authors_list(request):
   authors = Author.objects.all()
   form = AuthorForm()

   if request.method == "POST":
       form = AuthorForm(data=request.POST)
       if form.is_valid():
           form.save()
           messages.add_message(
               request,
               messages.SUCCESS,
               "New author added"
           )

   return render(
       request=request,
       template_name="posts/authors_list.html",
       context={"authors": authors, "form": form}
   )


def author_details(request, id):
   author = Author.objects.get(id=id)
   return render(
       request=request,
       template_name="posts/author_details.html",
       context={"author": author}
   )
