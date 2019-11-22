# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract ITem """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(AbstractItem):
    class Meta:
        verbose_name_plural = "Categories"


class Project(core_models.TimeStampedModel):

    """ Project Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    on_market = models.BooleanField(default=False)
    categories = models.ManyToManyField("Category", related_name="projects", blank=True)
    host = models.ForeignKey(
        "users.User", related_name="project_host", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(
        "users.User", related_name="project_members", blank=True
    )

    def __str__(self):
        return self.name

    def count_apply(self):
        return self.apply.count()


class ProjectJob(core_models.TimeStampedModel):

    """ Job Model Definition """

    name = models.CharField(max_length=140)
    start = models.TimeField()
    due = models.TimeField()
    charger = models.ForeignKey(
        "users.User", related_name="project_jobs", on_delete=models.SET_NULL, null=True
    )
    project = models.ForeignKey(
        "Project", related_name="project_jobs", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def is_finished(self):
        now = timezone.now().date()
        is_finished = now > self.due
        return is_finished
