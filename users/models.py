from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    