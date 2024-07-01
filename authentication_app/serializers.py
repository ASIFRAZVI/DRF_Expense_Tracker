from rest_framework import serializers
from .models import CustomUser

class auth_serializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"

class login_serializer(serializers.Serializer):
    username=serializers.CharField(max_length=200)
    password=serializers.CharField(max_length=200)
