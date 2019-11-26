from django.contrib import admin
from . import models

@admin.register(models.Contests)
class ApplyAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "day",
        "company"
    )
