from django.urls import path
from .views import greetings, greetings_name

urlpatterns = [
   path('', greetings),
   path('<str:name>/', greetings_name)
]
