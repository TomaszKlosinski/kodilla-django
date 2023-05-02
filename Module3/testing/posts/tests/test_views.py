from django.test import TestCase, Client

from posts.models import Author, Post

class IndexViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_authors_list(self):
        response = self.client.get("/posts/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h2>Homepage</h2>', response.content.decode())


class AuthorViewsTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="dummy", email="dummy@dummy.com")
        self.client = Client()

    def test_authors_list(self):
        response = self.client.get("/posts/a/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["authors"]), 1)
        self.assertIn('<li><a href="/posts/a/1">id:1, nick=dummy, email=dummy@dummy.com</a></li>', response.content.decode())

    def test_author_details(self):
        response = self.client.get("/posts/a/1", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('<td>dummy</td>', response.content.decode())
        self.assertIn('<td>dummy@dummy.com</td>', response.content.decode())


class PostViewsTest(TestCase):

    def setUp(self):
        a = Author.objects.create(nick="dummy", email="dummy@dummy.com")
        Post.objects.create(title="dummy", content="blah blah", author_id=a)
        self.client = Client()

    def test_postss_list(self):
        response = self.client.get("/posts/p/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 1)
        self.assertIn('<li><a href="/posts/p/1">id:1, title=dummy, author_id=dummy</a></li>', response.content.decode())

    def test_post_details(self):
        response = self.client.get("/posts/p/1", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('<td>dummy</td>', response.content.decode())
        self.assertIn('<td>blah blah</td>', response.content.decode())
