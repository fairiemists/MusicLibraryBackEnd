from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField(blank=True)
    genre = models.CharField(max_length=255)

