from django import forms
from blog.models import PostBook

class SeacrhForm(forms.ModelForm):
    class Meta:
        model = PostBook
        fields = ['name']



