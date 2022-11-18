from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth import models
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['username', 'email']


class SignUpSerializer(serializers.ModelSerializer):
    EMAIL_MAX_LENGTH = 80
    USERNAME_MAX_LENGTH = 45
    PASSWORD_MIN_LENGTH = 8

    email = serializers.CharField(
        max_length=EMAIL_MAX_LENGTH,
    )
    username = serializers.CharField(
        max_length=USERNAME_MAX_LENGTH,
    )
    password = serializers.CharField(
        min_length=PASSWORD_MIN_LENGTH,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError('Email has already been used')
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        print(token)
        return user
