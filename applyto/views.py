# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.views.generic import DetailView
from . import models
from participant import models as participant_models
from projects import models as project_models
from users import models as user_models


class CreateError(Exception):
    pass


def create(request, project_pk):
    try:
        the_project = project_models.Project.objects.get(pk=project_pk)
        models.Apply.objects.get(Q(project=project_pk) & Q(apply_user=request.user))
    except project_models.Project.DoesNotExist:
        messages.error(request, "해당 프로젝트는 존재하지 않습니다")
        raise redirect(reverse("core:home"))
    except models.Apply.DoesNotExist:
        models.Apply.objects.create(
            project=the_project, apply_user=request.user,
        )
        messages.success(request, "신청이 완료되었습니다")
        return redirect(reverse("projects:detail", kwargs={"pk": project_pk}))


def delete(request, project_pk):
    try:
        models.Apply.objects.filter(project=project_pk).filter(
            apply_user=request.user
        ).delete()
        messages.success(request, "신청이 취소되었습니다")
    except models.Apply.DoesNotExist:
        messages.error(request, "취소할수없습니다")
    return redirect(reverse("projects:detail", kwargs={"pk": project_pk}))


class ApplyDetailView(DetailView):
    model = models.Apply
    template_name = "applyto/apply_detail.html"


def toggle_applyto(request, pk):
    action = request.GET.get("action", None)
    the_apply = models.Apply.objects.get_or_none(pk=pk)
    if the_apply is not None and action is not None:
        if action == "accept":
            ck_dupl = (
                participant_models.Participant.objects.filter(user=the_apply.apply_user)
                .filter(project=the_apply.project)
                .exists()
            )
            if ck_dupl:
                models.Apply.objects.filter(pk=the_apply.pk).delete()
                messages.error(request, "이미 참가중인 프로젝트입니다")
            else:
                (
                    the_participant,
                    created,
                ) = participant_models.Participant.objects.get_or_create(
                    user=the_apply.apply_user, project=the_apply.project
                )
                models.Apply.objects.filter(pk=the_apply.pk).delete()
                messages.success(request, "참여신청을 수락하였습니다")
            return redirect(reverse("users:profile", kwargs={"pk": request.user.pk}))
        if action == "denied":
            models.Apply.objects.filter(pk=the_apply.pk).delete()
            messages.success(request, "참여신청을 거절하였습니다")
            return redirect(reverse("users:profile", kwargs={"pk": request.user.pk}))

