from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.OneToOneField(
        "users.User", related_name="list", on_delete=models.CASCADE
    )
    projects = models.ManyToManyField("projects.Project", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_projects(self):
        return self.projects.count()

    count_projects.short_description = "Number of Projects"
