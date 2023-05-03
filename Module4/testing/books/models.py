from django.db import models

class Book(models.Model):
   title = models.CharField(max_length=20)
   author_id = models.ForeignKey('books.Author', on_delete=models.CASCADE, null=True, blank=True)
   image = models.ImageField(upload_to='photos/%Y/%m/%d')
   tags = models.ManyToManyField("books.Tag", related_name="books")
   created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return f"id:{self.id}, title={self.title}, author_id={self.author_id.name}, tags={self.tags}"


class Author(models.Model):
   name = models.CharField(max_length=20)
   created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return f"id:{self.id}, name={self.name}"


class Tag(models.Model):
   word = models.CharField(max_length=50, unique=True)
   created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return f"id:{self.id}, title={self.word}"
