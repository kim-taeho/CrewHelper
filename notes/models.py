# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import requests
from django.urls import reverse
from bs4 import BeautifulSoup
from core import models as core_models


class Notes(core_models.TimeStampedModel):

    """ Apply Model Definition """

    title = models.CharField(max_length=400)
    company = models.CharField(max_length=400, blank=True)
    day = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse("notes:update", kwargs={"pk": self.pk})

