from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """IN PROGRESS..."""

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
