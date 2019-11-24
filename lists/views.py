from django.shortcuts import render, redirect, reverse
from projects import models as project_models
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . import models


def toggle_project(request, project_pk):
    action = request.GET.get("action", None)
    project = project_models.Project.objects.get_or_none(pk=project_pk)
    if project is not None and action is not None:
        the_list, created = models.List.objects.get_or_create(
            user=request.user, name="My Favourite Projects"
        )
        if action == "add":
            the_list.projects.add(project)
            messages.info(request, "즐겨찾기에 추가되었습니다")
        elif action == "remove":
            the_list.projects.remove(project)
            messages.info(request, "즐겨찾기에서 삭제되었습니다")
    return redirect(reverse("projects:detail", kwargs={"pk": project_pk}))

class SeeFavsView(TemplateView):

    template_name = "lists/list_detail.html"
