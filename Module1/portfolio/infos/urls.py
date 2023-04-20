from django.urls import path
from .views import index, about, contact

urlpatterns = [
   path('', index),
    path('me', about),
    path('contact', contact),
]