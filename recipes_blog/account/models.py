from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to have is_staff being True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have is_superuser being True')

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    EMAIL_MAX_LENGTH = 80
    USERNAME_MAX_LENGTH = 45

    email = models.CharField(
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
    )
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
