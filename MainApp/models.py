from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.TextField(max_length=1000)
