from django.shortcuts import render
from django.views.generic import ListView

from book.models import PostBook


class IndexListView(ListView):
    model = PostBook
    template_name = "index.html"


