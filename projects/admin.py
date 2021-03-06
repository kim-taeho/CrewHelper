# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    """ Categoty Admin Definition """

    list_display = ("name",)

    def used_by(serlf, obj):
        return obj.projects.count()


@admin.register(models.ProjectJob)
class ProjectJobAdmin(admin.ModelAdmin):

    """ Project Job Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "start",
                    "due",
                    "charger",
                    "project",
                    "isFinished",
                    "howLate",
                    "importance",
                )
            },
        ),
    )

    list_display = (
        "project",
        "name",
        "start",
        "due",
        "charger",
        "isFinished",
        "howLate",
    )

    raw_id_fields = (
        "charger",
        "project",
    )

    search_fields = ("^charger__username",)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    """ Project Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "categories", "host", "on_market",)},
        ),
    )

    list_display = (
        "name",
        "host",
        "on_market",
    )

    raw_id_fields = ("host",)

    filter_horizontal = ("categories",)


@admin.register(models.JobContribution)
class JobContribution(admin.ModelAdmin):

    """ Job Contribution Admin Def."""

    fieldsets = (
        ("Basic Info", {"fields": ("inProject", "inProjectJob", "inCharge","score",)},),
    )
