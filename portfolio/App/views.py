from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.


def inicio(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')


class List_project(ListView):

    model=Project

    template_name='App/projects.html'