from django import forms
from django.contrib.admin import widgets
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
            "importance",
        )

    """ def __init__(self, *args, **kwargs):
        super(CreateProjectJobForm, self).__init__(*args, **kwargs)
        self.fields['start'].widget = widgets.AdminDateWidget()
        self.fields['due'].widget = widgets.AdminTimeWidget() """

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
