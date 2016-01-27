from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic.detail import DetailView

from .models import PostBook

class BookListView(ListView):
    model = PostBook
    template_name = "book.html"

class BookDetailView(DetailView):
    model = PostBook
    template_name ="book-detail.html"
    slug_field = 'slug'
