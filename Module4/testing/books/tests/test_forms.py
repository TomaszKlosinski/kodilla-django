from django.test import TestCase

from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author


class AuthorFormTest(TestCase):

    def test_author_save_correct_data(self):
        self.assertEqual(len(Author.objects.all()), 0)

        data = {"nick": "dummy", "email": "dummy@dummy.com"}
        form = AuthorForm(data=data)

        self.assertTrue(form.is_valid())

        a = form.save()

        self.assertIsInstance(a, Author)
        self.assertEqual(a.nick, "dummy")
        self.assertIsNotNone(a.id)
