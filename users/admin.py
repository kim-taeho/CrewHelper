# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ("gender", "bio", "major", "login_method",),},),
    )

    list_display = (
        "username",
        "email",
        "major",
        "gender",
        "login_method",
    )
