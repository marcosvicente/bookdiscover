from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class PostBook(models.Model):
    name = models.CharField(max_length= 100)
    slug  = models.SlugField()
    year = models.IntegerField()
    whiter = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.FileField(upload_to='media/post-book' )
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.name


class CometaryBook(models.Model):
    username = models.ForeignKey(User)
    post = models.ForeignKey(PostBook)
    text = models.TextField()
    like = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class CometaryBookForm(forms.ModelForm):
    class Meta:
        model = CometaryBook
        fields = ['username', 'text', 'like']
