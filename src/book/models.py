from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PostBook(models.Model):
    name = models.CharField(max_length= 100)
    year = models.IntegerField()
    whiter = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='media/post-book' )
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.name

