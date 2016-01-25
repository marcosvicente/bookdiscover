from django.shortcuts import render
from django.contrib.auth import login

def index(request):
     
    return render(request, 'index.html')


