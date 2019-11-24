# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from . import models
from projects import models as project_models
from users import models as user_models



class CreateError(Exception):
    pass


def create(request, project_pk):
    try:
        the_project = project_models.Project.objects.get(pk=project_pk)
        models.Apply.objects.get(
            Q(project=project_pk) & Q(apply_user=request.user)
            )
    except project_models.Project.DoesNotExist:
        messages.error(request, "해당 프로젝트는 존재하지 않습니다")
        raise redirect(reverse("core:home"))
    except models.Apply.DoesNotExist:
        models.Apply.objects.create(
            project=the_project,
            apply_user=request.user,
        )
        return redirect(reverse("projects:detail", kwargs={"pk": project_pk}))
        
