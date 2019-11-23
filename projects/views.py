# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ HomeView """

    model = models.Project
    paginate_by = 12
    paginate_orphans = 2
    context_object_name = "projects"
    template_name = "projects/home.html"


class ProjectDetail(DetailView):

    """ Project Detail View """

    model = models.Project
    context_object_name = "project"
    template_name = "projects/project-detail.html"
