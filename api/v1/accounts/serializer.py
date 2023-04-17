from accounts.models import Profile
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    phone = serializers.CharField()
    fullname = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'name',
            'phone'
            'username'
        )

class ChiefProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    