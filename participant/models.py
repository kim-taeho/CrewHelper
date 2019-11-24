from django.db import models
from core import models as core_models


class Participant(core_models.TimeStampedModel):

    """ Participant Model Deifinitino """

    user = models.ForeignKey(
        "users.User", related_name="participants", on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        "projects.Project", related_name="participants", on_delete=models.CASCADE
    )
