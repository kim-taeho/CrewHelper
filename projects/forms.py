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


class CreateProjectJobForm(forms.ModelForm):
    class Meta:
        model = models.ProjectJob
        fields = (
            "name",
            "start",
            "due",
        )

    def save(self):
        projectjob = super().save(commit=False)
        return projectjob


class SearchForm(forms.Form):

    name = forms.CharField(initial="Project Name")
    categories = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
