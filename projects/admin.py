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
                    )},
        ),
    )

    list_display = (
        "project",
        "name",
        "start",
        "due",
        "charger",
        "is_finished",
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
            {
                "fields": (
                    "name",
                    "description",
                    "categories",
                    "host",
                    "members",
                    "on_market",
                )
            },
        ),
    )

    list_display = (
        "name",
        "host",
        "on_market",
        "count_apply",
    )

    raw_id_fields = ("host",)

    filter_horizontal = (
        "categories",
        "members",
    )

    def count_members(self, obj):
        return obj.members.count()
