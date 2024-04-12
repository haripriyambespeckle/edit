from django.contrib.auth.models import User
from rest_framework import serializers
from 


class UserSerializer(serializers.ModelSerializer)
    class Meta:
        model = User
        field = ['id', '']
