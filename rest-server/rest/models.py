from django.db import models

# Create your models here.

class History(models.Model):
    success = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    result = models.IntegerField(default=0)
