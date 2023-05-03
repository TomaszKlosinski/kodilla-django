from django.urls import path

from greetings.views import greetings, greetings_name, about, contact

urlpatterns = [
       path('', greetings, name="welcome"),
       path('<str:name>/', greetings_name),
       path('about/', about, name="about"),
       path('contact/', contact, name="contact"),
]
