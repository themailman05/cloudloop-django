from django.db import models
from django.contrib.auth.models import AbstractUser

from realtimechatserver import helper

# Create your models here.

class User(AbstractUser):
    """Extend User functionality"""
    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)



