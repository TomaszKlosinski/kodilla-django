from django import forms
from .models import Author

class AuthorForm(forms.Form):
   nick = forms.CharField(required=True)
   email = forms.EmailField(required=False)

   def clean(self):
       cleaned_data = super().clean()
       nick = cleaned_data.get('nick')
       email = cleaned_data.get('email')

       if not nick:
           raise forms.ValidationError("Nick cannot be empty")


class PostForm(forms.Form):
   title = forms.CharField(required=True)
   content = forms.CharField(widget=forms.Textarea)
   author = forms.ChoiceField(
       choices=((a.id, a.nick) for a in Author.objects.all())
    )

   def clean(self):
       cleaned_data = super().clean()
       title = cleaned_data.get('nick')
       content = cleaned_data.get('email')
       author = cleaned_data.get('author')

       if not title:
           raise forms.ValidationError("Title cannot be empty")
