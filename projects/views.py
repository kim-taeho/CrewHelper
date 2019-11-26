# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView, View
from django.contrib import messages
from users import mixins as user_mixins
from participant import models as participant_models
from . import forms
from . import models
from . import forms
from contests import models as contest_models


class HomeView(ListView):

    """ HomeView """

    model = models.Project
    paginate_by = 12
    paginate_orphans = 2
    context_object_name = "projects"
    template_name = "projects/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update(
            {"contests": contest_models.Contests.objects.all()[:12],}
        )
        return context


class ProjectDetail(DetailView):

    """ Project Detail View """

    model = models.Project
    context_object_name = "project"
    template_name = "projects/project-detail.html"


class CreateProjectView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateProjectForm
    template_name = "projects/project_create.html"

    def form_valid(self, form):
        project = form.save()
        project.host = self.request.user
        project.save()

        messages.success(self.request, "프로젝트가 생성되었습니다")
        return redirect(reverse("projects:detail", kwargs={"pk": project.pk}))


class ProjectMemberDetail(user_mixins.LoggedInOnlyView, View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        project = models.Project.objects.get_or_none(pk=pk)
        if not project:
            raise Http404()
        project_job = models.ProjectJob.objects.filter(project=project)
        participants = participant_models.Participant.objects.filter(project=project)
        form = forms.CreateProjectJobForm()
        return render(
            self.request,
            "projects/member_project.html",
            {
                "project": project,
                "participants": participants,
                "project_job": project_job,
                "form": form,
            },
        )


def create_job(request, project_pk):
    if request.method == "POST":
        form = forms.CreateProjectJobForm(request.POST)
        project = models.Project.objects.get_or_none(pk=project_pk)
        if not project:
            return redirect(reverse("core:home"))
        if form.is_valid():
            job = form.save()
            job.charger = request.user
            job.project = project
            job.save()
            messages.success(request, "업무가 생성되었습니다")
            return redirect(
                reverse("projects:member-detail", kwargs={"pk": project_pk})
            )


def toggle_market(request, pk):
    the_project = models.Project.objects.get_or_none(pk=pk)
    if the_project.on_market is True:
        the_project.on_market = False
        the_project.save()
        messages.success(request, "공고등록을 마갑하였습니다")
    else:
        the_project.on_market = True
        the_project.save()
        messages.success(request, "공고를 등록하였습니다")
    return redirect(reverse("projects:member-detail", kwargs={"pk": pk}))

