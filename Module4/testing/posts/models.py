from django.db import models

class Post(models.Model):
   title = models.CharField(max_length=20)
   content = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now_add=True)
   author_id = models.ForeignKey('posts.Author', on_delete=models.CASCADE, null=True, blank=True)
   image = models.ImageField(upload_to='photos/%Y/%m/%d')
   tags = models.ManyToManyField("posts.Tag", related_name="posts")

   def __str__(self):
        return f"id:{self.id}, title={self.title}, author_id={self.author_id.nick}"


class Author(models.Model):
   nick = models.CharField(max_length=5)
   email = models.EmailField()

   def __str__(self):
        return f"id:{self.id}, nick={self.nick}, email={self.email}"


class Tag(models.Model):
   word = models.CharField(max_length=50, unique=True)
   created = models.DateTimeField(auto_now_add=True)
