from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about', about, name='about'),
    path('projects', List_project.as_view(), name='projects'),
    path('login', iniciar_sesion, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('create project', CreateProject.as_view(), name='create_project'),
    path('project/<int:pk>', DetalleProject.as_view(), name='project_detail')
]
