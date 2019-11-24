from django import forms
from . import models


class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = models.Project
        fields = (
            "name",
            "description",
            "categories",
        )
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "description": forms.TextInput(attrs={"placeholder": "Description"}),
        }
        
    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project

