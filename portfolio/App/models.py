from django.db import models

# Create your models here.

class Project(models.Model):

    def __str__(self):

        return f'Project {self.name}'

    name=models.CharField(max_length=30)
    repository=models.CharField(max_length=300, blank=True, null=True)
    description=models.CharField(max_length=300)
    functionalities=models.CharField(max_length=300)
    used_tools=models.CharField(max_length=300)
    git_page=models.CharField(max_length=300, blank=True, null=True)

class Image(models.Model):

    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='img_proyect', null=True, blank=True)

    
    def __str__(self):

        return f'Project {self.project.name}'