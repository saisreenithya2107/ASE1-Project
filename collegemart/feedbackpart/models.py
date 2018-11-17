from django.db import models

class Userlog(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    comments=models.CharField(max_length=500)

