from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

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
    
class BookListCategory(TemplateView):
    model = PostBook
    template_name = "category-all.html"

class BookListCategoryAventura(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="AVENTURA")
    template_name = 'category-aventura.html'

class BookListCategoryRomance(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="ROMANCE")
    template_name = 'category-romance.html'   

class BookListCategoryPoesia(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="POESIA")
    template_name = 'category-poesia.html'   

class BookListCategoryFiccaoCientifica(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="FICCAO CIENTIFICA")
    template_name = 'category-ficcao-cientifica.html'   


class BookListCategoryTerror(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="TERROR")
    template_name = 'category-terror.html'   

class BookListCategoryFantasia(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="FANTASIA")
    template_name = 'category-fantasia.html' 


class BookListCategoryComedia(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="COMEDIA")
    template_name = 'category-comedia.html' 


class BookListCategoryAutoAjuda(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="AUTO AJUDA")
    template_name = 'categoria-auto-ajuda.html' 

class BookListCategoryRomancePolicial(ListView):
    model = PostBook
    queryset = PostBook.objects.filter(category="ROMANCE POLICIAL")
    template_name = 'categoria-romance-policial.html'

