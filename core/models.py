from django.db import models
from django.contrib.auth.models import User


class Stamp(models.Model):
    """Stamp"""
    key = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    short_description = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)
    image_url = models.URLField()
    url = models.URLField(blank=True)
    user = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.name
