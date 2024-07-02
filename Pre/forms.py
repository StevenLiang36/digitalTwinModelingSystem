from django import forms
from django.forms import modelformset_factory
from .models import Project, Image, ThreeDModel


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control background-dark', 'style': 'color:white;'}),
            'description': forms.Textarea(attrs={'class': 'form-control background-dark', 'style': 'color:white;'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(ProjectForm, self).__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] += ' text-white'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']


ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=5)


class ThreeDModelForm(forms.ModelForm):
    class Meta:
        model = ThreeDModel
        fields = ['model_file']
