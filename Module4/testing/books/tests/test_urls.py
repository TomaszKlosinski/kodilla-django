from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404

from posts.views import index, posts_list, post_details, authors_list, author_details

class PostsUrlsTest(TestCase):
   def test_resolution_for_index(self):
       resolver = resolve('/posts/')
       self.assertEqual(resolver.func, index)

   def test_resolution_for_posts_list(self):
       resolver = resolve('/posts/p/')
       self.assertEqual(resolver.func, posts_list)

   def test_resolution_for_post_details(self):
       resolver = resolve('/posts/p/1')
       self.assertEqual(resolver.func, post_details)

   def test_argument_for_post_details_should_be_integer_or_404(self):
       with self.assertRaises(Resolver404):
           resolve('/posts/p/abc')

   def test_resolution_for_authors_list(self):
       resolver = resolve('/posts/a/')
       self.assertEqual(resolver.func, authors_list)

   def test_resolution_for_author_details(self):
       resolver = resolve('/posts/a/1')
       self.assertEqual(resolver.func, author_details)

   def test_argument_for_author_details_should_be_integer_or_404(self):
       with self.assertRaises(Resolver404):
           resolve('/posts/a/abc')
