from django.db import models
from django.contrib.auth.models import User

class LabUser(models.Model):
    user = models.ForeignKey(User)
    password = models.CharField(max_length=64)
