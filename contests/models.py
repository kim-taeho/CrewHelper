from django.db import models


class Contests(models.Model):

    """ Contest Scarpe Model Definition """
    title = models.CharField(max_length=400)
    company = models.CharField(max_length=400)
    day = models.CharField(max_length=400)

    def __str__(self):
        return self.title

