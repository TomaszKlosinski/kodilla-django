from django import forms
from .models import Author, Post


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = "__all__"
       fields = ["title", "content", "author_id", "image", "tags"]
