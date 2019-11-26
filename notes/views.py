# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
import requests
from django.http import Http404
from . import models
from . import forms
from projects import models as project_models
from users import models as user_models
from bs4 import BeautifulSoup




def create_view(request):
    form = forms.ConModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "contests/create.html", context)


def list_view(request):
    contests = models.Apply.objects.all()
    context = {
        'object_list': contests
    }
    return render(request, "contests/list.html", context)


def update_view(request, pk):
    unique_contest = get_object_or_404(models.Apply, pk=pk)
    form = forms.ConModelForm(request.POST or None, request.FILES or None, instance=unique_contest)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "contests/create.html", context)
