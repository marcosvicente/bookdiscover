from django.contrib import admin
from .models import PostBook

class PostBookAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'

admin.site.register(PostBook, PostBookAdmin)
