from django.test import TestCase, Client

class GreetingsViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_greetings(self):
        response = self.client.get("/greetings/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('World', response.content.decode())

    def test_greetings_name(self):
        response = self.client.get("/greetings/tomasz", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tomasz', response.content.decode())
