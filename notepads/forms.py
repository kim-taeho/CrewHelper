from django import forms
from . import models


class ConModelForm(forms.ModelForm):

    """ Contest Form Definition """

    class Meta:
        model = models.Notes
        fields = ["title", "company", "day"]

