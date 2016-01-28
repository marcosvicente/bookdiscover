from django import forms

from blog.models import PostBook

class PostBookFormSearch(forms.ModelForm):
    class Meta:
        model = PostBook
        fields = ['name']

