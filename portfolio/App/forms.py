from django import forms
from .models import *
from django.forms.models import inlineformset_factory


class ImageForm(forms.ModelForm):

    #image=forms.ImageField(label='Image')

    class Meta:
        model=Image
        exclude=()
        widgets = {
        'image': forms.ClearableFileInput(attrs={"multiple": True})
       }

class ProjectForm(forms.ModelForm):

    class Meta:
        model=Project
        fields=['name', 'repository', 'description', 
        'functionalities', 'used_tools', 'git_page',]

ImageFormSet= inlineformset_factory(
    Project, Image, form=ImageForm,
    fields=['image'], extra=7, can_delete=True
)