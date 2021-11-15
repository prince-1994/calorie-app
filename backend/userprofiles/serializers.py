from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'