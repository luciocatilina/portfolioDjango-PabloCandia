from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about', about, name='about'),
    path('projects', List_project.as_view(), name='projects')
]
