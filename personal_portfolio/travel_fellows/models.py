from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, default='name')
    surname = models.CharField(max_length=120, default='surename')
    email = models.EmailField(max_length=100, unique=True, default='my@mail.com')
    password = models.CharField(max_length=120, default='1111')


class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
