# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.contrib import admin


@admin.register(models.Apply)
class ApplyAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "apply_user",
    )
