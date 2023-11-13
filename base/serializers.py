from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'birth_date', 'address', 'gender', 'phone_num', 'email', 'password', 'department',
                  'position', 'role']

    def create(self, validated_data):
        #validated_data['password'] = make_password(validated_data.get('password'))
        return User.objects.create_user(**validated_data)