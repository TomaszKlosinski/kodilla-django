from django.contrib import admin
from django.urls import include, path
from infos.views import index

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include("infos.urls")),
]