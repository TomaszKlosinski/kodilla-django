from django.contrib import admin
from django.urls import path
from greetings.views import greetings, greetings_name


urlpatterns = [
   path('admin/', admin.site.urls),
   path('greetings/', greetings),
   path('greetings/<str:name>/', greetings_name)
]
