from django.shortcuts import render
from django.views.generic import ListView

from .models import PostBook

class BookListView(ListView):
    model = PostBook
    template_name = "book.html"

