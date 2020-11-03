from django.db import models

class Contest(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=2000)
    active = models.BooleanField(default=False)

