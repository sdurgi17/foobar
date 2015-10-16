from django.contrib.gis.db import models


class User(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    organisation = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    session_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

