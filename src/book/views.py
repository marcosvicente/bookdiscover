from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from rest_framework import viewsets

from .models import PostBook, CometaryBook, CometaryBookForm

class BookListView(ListView):
    model = PostBook
    template_name = "book.html"

class BookDetailView(DetailView):
    model = PostBook
    template_name ="book-detail.html"
    slug_field = 'slug'
   
class ComentFormView(FormView):
    template_name = 'book-detail.html'
    form_class = CometaryBookForm
    

