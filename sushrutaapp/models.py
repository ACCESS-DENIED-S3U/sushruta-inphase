from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Users(models.Model):  # extended user model
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    phone = models.IntegerField(default=0)
    Address = models.CharField(default='', max_length=50)
    u_are = models.CharField(default='', max_length=25)