from django.db import models

# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length= 50)
    purchaser = models.CharField(max_length=50)
    description = models.TextField(default='snack')