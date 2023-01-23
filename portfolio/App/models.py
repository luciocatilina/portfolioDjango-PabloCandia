from django.db import models

# Create your models here.

class Project(models.Model):

    def __str__(self):

        return f'Project {self.name}'

    name=models.CharField(max_length=30)
    repository=models.CharField(max_length=300)
    description=models.CharField(max_length=300, default='textoooo')
    git_page=models.CharField(max_length=300, blank=True)
    image=models.ImageField(upload_to='img_proyect')