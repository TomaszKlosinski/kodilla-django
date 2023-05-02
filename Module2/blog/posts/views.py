from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from posts.models import Post, Author
from posts.forms import AuthorForm, PostForm

def index(request):
    c = {"title": "Homepage"}
    return render(
        request=request,
        template_name="posts/home.html",
        context=c
    )


def posts_list(request):
   if request.method == "POST":
       title = request.POST['title'] or None
       content = request.POST['content'] or ''
       author_id = request.POST['author'] or None
       author = Author.objects.get(pk=int(author_id))

       if not title or not author:
           messages.add_message(request, messages.ERROR, "Error!")
       else:
           Post.objects.get_or_create(
               title=title,
               content=content,
               author_id=author
           )
           messages.add_message(request, messages.SUCCESS, "Success!")

   posts = Post.objects.all()
   post_form = PostForm()
   return render(
       request=request,
       template_name="posts/posts_list.html",
       context={"posts": posts, "form": post_form}
   )


def post_details(request, id):
   post = Post.objects.get(id=id)
   return render(
       request=request,
       template_name="posts/post_details.html",
       context={"post": post}
   )


def authors_list(request):
   if request.method == "POST":
       nick = request.POST['nick'] or None
       email = request.POST['email'] or ''

       if not nick:
           messages.add_message(request, messages.ERROR, "Error!")
       else:
           Author.objects.get_or_create(
               nick=nick,
               email=email
           )
           messages.add_message(request, messages.SUCCESS, "Success!")

   authors = Author.objects.all()
   author_form = AuthorForm()
   return render(
       request=request,
       template_name="posts/authors_list.html",
       context={"authors": authors, "form": author_form}
   )


def author_details(request, id):
   author = Author.objects.get(id=id)
   return render(
       request=request,
       template_name="posts/author_details.html",
       context={"author": author}
   )
