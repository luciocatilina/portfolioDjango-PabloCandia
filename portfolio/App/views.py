from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.db import transaction

# Create your views here.


def inicio(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')


class List_project(ListView):

    model=Project

    template_name='App/projects.html'

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.all().order_by('-pk')

def iniciar_sesion(request):

    if request.method == 'POST':

        form_login = MyAuthForm(request, data=request.POST)

        if form_login.is_valid():

            usuario = form_login.cleaned_data.get('username')
            contra = form_login.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user:
                login(request, user)
                return redirect('create_project')
            else:
                return render(request, 'App/index.html')
    else:
        form_login = MyAuthForm()

    return render(request, 'App/login.html', {'form_login': form_login})

class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': gettext_lazy(
            'Usuario y/o contraseña incorrectos'
        )
    }

class CreateProject(LoginRequiredMixin, CreateView):

    model=Project

    template_name='App/create_project.html'

    form_class=ProjectForm

    def get_context_data(self, **kwargs):
        data = super(CreateProject, self).get_context_data(**kwargs)
        data['form_images'] = ImageFormSet()
        if self.request.POST:
            data['form_images'] = ImageFormSet(self.request.POST, self.request.FILES)
        else:
            data['form_images'] = ImageFormSet()
        return data