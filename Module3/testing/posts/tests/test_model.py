from django.test import TestCase
from posts.models import Author, Post


class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="dummy", email="dummy@dummy.com")

    def test_author_str(self):
        a = Author.objects.get(id=1)

        self.assertEqual(str(a), "id:1, nick=dummy, email=dummy@dummy.com")


class PostModelTest(TestCase):

    def setUp(self):
        a = Author.objects.create(nick="dummy", email="dummy@dummy.com")
        p = Post.objects.create(title='dummy', content='blah blah', author_id=a)

    def test_result_str(self):
        p = Post.objects.get(id=1)

        self.assertEqual(str(p), 'id:1, title=dummy, author_id=dummy')
