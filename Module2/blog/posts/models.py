from django.db import models

class Post(models.Model):
   title = models.CharField(max_length=20)
   content = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now_add=True)
   author_id = models.ForeignKey('posts.Author', on_delete=models.CASCADE, null=True, blank=True)

class Author(models.Model):
   nick = models.CharField(max_length=5)
   email = models.EmailField()
