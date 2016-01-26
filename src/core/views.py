from django.shortcuts import render
from django.views.generic import ListView

from book.models import PostBook

def IndexListView(TemplateView):
    template_name = "index.html"

