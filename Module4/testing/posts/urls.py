from django.urls import path
from .views import index, posts_list, post_details, authors_list, author_details

app_name="posts"
urlpatterns = [
   path('', index),
   path('p/', posts_list, name="posts_list"),
   path('p/<int:id>', post_details, name="post_details"),
   path('a/', authors_list, name="authors_list"),
   path('a/<int:id>', author_details, name="author_details"),
]
