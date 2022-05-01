from django.db import models

class Post(models.Model):
    URL = models.CharField(blank=True, max_length=1000)
    myKey = models.TextField(null=True)
    myList = models.TextField(null=True)

