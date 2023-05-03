from rest_framework import routers
from posts import api_views as posts_views
from books import api_views as books_views


posts_router = routers.DefaultRouter()
posts_router.register('posts', posts_views.PostViewset)
posts_router.register('authors', posts_views.AuthorViewset)

books_router = routers.DefaultRouter()
books_router.register('books', books_views.BookViewset)
books_router.register('authors', books_views.AuthorViewset)
