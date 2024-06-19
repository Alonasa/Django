from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)
    surname = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=120)


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.FilePathField(default='photos/default.jpg')
    hashtags = ArrayField(models.CharField(max_length=300), blank=False, default=list)
    destinations = ArrayField(models.CharField(max_length=200), blank=False, default=list)
    level = models.IntegerField(default=1)
    likes_count = models.IntegerField(default=0)
    hobbies = ArrayField(models.CharField(max_length=300), blank=False, default=list)
    music = ArrayField(models.CharField(max_length=300), blank=False, default=list)
    food = ArrayField(models.CharField(max_length=300), blank=False, default=list)
    transport = ArrayField(models.CharField(max_length=300), blank=False, default=list)


class UserPlans(models.Model):
    id = models.AutoField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    destinations = ArrayField(models.CharField(max_length=100), blank=False, default=list)
    plans = ArrayField(models.CharField(max_length=1000), blank=False, default=list)
    companions = models.IntegerField(default=1)
    dates_start = models.DateField()
    dates_end = models.DateField()
    kids = models.BooleanField(default=False)






