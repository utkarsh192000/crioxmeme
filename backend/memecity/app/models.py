from django.db import models

# Create your models here.
class Meme(models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    url = models.URLField(max_length=1000000)
  