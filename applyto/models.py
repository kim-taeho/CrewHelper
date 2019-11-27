# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from core import models as core_models


class Apply(core_models.TimeStampedModel):

    """ Apply Model Definition """

    project = models.ForeignKey(
        "projects.Project", related_name="apply", on_delete=models.CASCADE
    )
    apply_user = models.ForeignKey(
        "users.User", related_name="apply_user", on_delete=models.CASCADE
    )
    applyto = models.ForeignKey(
        "users.User", related_name="applyto", on_delete=models.CASCADE, null=True
    )

