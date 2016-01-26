from __future__ import unicode_literals

from django.db import models
    
class PostBook(models.Model):
    name = models.CharField(max_length= 100)
    year = models.IntegerField()
    whiter = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField()
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

