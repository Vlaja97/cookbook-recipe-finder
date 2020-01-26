from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

