from django.db import models

class Url(models.Model):
    original_url = models.URLField(max_length=2000, unique=True)
    encoded_url = models.URLField(blank=True,null=True)