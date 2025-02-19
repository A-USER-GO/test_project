from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    name = models.CharField(max_length=120, verbose_name='用户昵称')
    age = models.PositiveIntegerField(verbose_name='用户年龄')