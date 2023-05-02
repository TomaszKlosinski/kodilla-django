from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404

from greetings.views import greetings, greetings_name

class GreetingsUrlsTest(TestCase):

   def test_resolution_for_greetings(self):
       resolver = resolve('/greetings/')
       self.assertEqual(resolver.func, greetings)


   def test_resolution_for_greetings_name(self):
       resolver = resolve('/greetings/tomasz/')
       self.assertEqual(resolver.func, greetings_name)
