from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.urls import reverse_lazy
from django.db import transaction
from django.db.models import Count

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
    
    def get_context_data(self, **kwargs):
        
        lista_ids=Project.objects.all().values_list('id', flat=True)
        portada = list()
        context = super(List_project, self).get_context_data(**kwargs)
        for i in lista_ids:
            if Image.objects.select_related('project').filter(project_id = i):
                portada.append(Image.objects.select_related('project').filter(project_id = i)[0])
                context['portadas'] = portada
        return context

class DetalleProject(DetailView):

    model=Project

    template_name='App/detalle_project.html'

    def get_context_data(self, **kwargs):
        context=super(DetalleProject, self).get_context_data(**kwargs)
        context['projects']=Project.objects.filter(pk=self.kwargs['pk'])
        context['images']=Image.objects.select_related('project').filter(project_id = self.kwargs['pk']).order_by('pk')
        x=len(list(Image.objects.select_related('project').filter(project_id = self.kwargs['pk'])))
        lista_total_imagenes=list()
        for i in range(x):
            lista_total_imagenes.append(str(i))
        context['total']=''.join(lista_total_imagenes)

        return context
        
    

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

    success_url= reverse_lazy('inicio')
    #'''
    def get_context_data(self, **kwargs):
        context = super(CreateProject, self).get_context_data(**kwargs)
        context['form_images'] = ImageFormSet()
        if self.request.POST:
            context['form_images'] = ImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['form_images'] = ImageFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form_img = context['form_images']
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if form_img.is_valid():
                form_img.instance = self.object
                form_img.save()
        return super(CreateProject, self).form_valid(form)
    #'''
