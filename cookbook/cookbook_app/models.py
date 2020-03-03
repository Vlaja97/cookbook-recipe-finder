from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.FileField(null=True, blank=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    #def __str__(self):
        #return self.name