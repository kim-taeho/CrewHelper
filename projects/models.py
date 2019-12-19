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

    def __str__(self):
        return self.name

    def count_apply(self):
        return self.apply.count()

    def get_first_category(self):
        try:
            category, = self.categories.all()[:1]
            return category
        except ValueError:
            return None

    def get_second_category(self):
        try:
            category, = self.categories.all()[1:2]
            return category
        except ValueError:
            return None

    def count_participants(self):
        return self.participants.count() + 1


class ProjectJob(core_models.TimeStampedModel): 

    """ Job Model Definition """

    LOW = 1
    MIDDLELOW = 2
    MIDDLE = 3
    MIDDLEHIGH = 4
    HIGH = 5

    IMPORTANCE_CHOICES = (
        (LOW, 1),
        (MIDDLELOW, 2),
        (MIDDLE, 3),
        (MIDDLEHIGH, 4),
        (HIGH, 5),
    )
    name = models.CharField(max_length=140)
    start = models.DateField()
    isFinished = models.BooleanField(default=False)
    howLate = models.IntegerField(default=0, null=True)
    due = models.DateField()
    charger = models.ForeignKey(
        "users.User", related_name="project_jobs", on_delete=models.SET_NULL, null=True,
    )
    project = models.ForeignKey(
        "Project", related_name="project_jobs", on_delete=models.CASCADE
    )
    charger_true = models.BooleanField(default=False)
    importance = models.IntegerField(choices=IMPORTANCE_CHOICES, default=LOW)

    def __str__(self):
        return self.name

    def is_finished(self):
        # now = timezone.now().date()
        if(self.isFinished is True):
            self.isFinished = False
        else:
            self.isFinished = True
        return self.isFinished


class JobContribution(core_models.TimeStampedModel): 

    """ Job Contribution Model Definition """

    inProject = models.ForeignKey(
        "Project", related_name="job_contribution", on_delete=models.CASCADE
    )
    inProjectJob = models.ForeignKey(
        "ProjectJob", related_name="job_contribution", on_delete=models.CASCADE, null=True
    )
    inCharge = models.ForeignKey(
        "users.User", related_name="job_contribution", on_delete=models.CASCADE, null=True
    )
    score = models.FloatField(default=0)
