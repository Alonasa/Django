from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)
    surname = models.CharField(max_length=120, null=False)
    username = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=120)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="travel_fellows/profile/", blank=True)
    destinations = ArrayField(models.CharField(max_length=200), blank=False, default=list)
    level = models.IntegerField(default=1)
    likes_count = models.IntegerField(default=0)
    hobbies = ArrayField(models.CharField(max_length=300), blank=False, default=list)
    music = ArrayField(models.CharField(max_length=300), blank=False, default=list)
    food = ArrayField(models.CharField(max_length=300), blank=False, default=list)


class HashTag(models.Model):
    hashtag = models.CharField(max_length=100, unique=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.hashtag}'


class UserTransportation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transportation')
    plane = models.BooleanField(default=False)
    bus = models.BooleanField(default=False)
    bike = models.BooleanField(default=False)
    feet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name}'s transportation"


class UserPlans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destinations = ArrayField(models.CharField(max_length=100), blank=False, default=list)
    plans = ArrayField(models.CharField(max_length=1000), blank=False, default=list)
    companions = models.IntegerField(default=1)
    length = models.IntegerField(default=1)
    dates_start = models.DateField()
    dates_end = models.DateField()
    kids = models.BooleanField(default=False)
