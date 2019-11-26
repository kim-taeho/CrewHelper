# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.contrib import admin


@admin.register(models.Notes)
class NotesAdmin(admin.ModelAdmin):

    list_display = ("title", "day", "company")
