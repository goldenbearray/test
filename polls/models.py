from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Resolution_action(models.Model):

    label = models.CharField(
        max_length=255,
    )
    resolution = models.TextField()


    def __str__(self):
        return self.label