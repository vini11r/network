from rest_framework import serializers

from users.models import User
from users.validators import user_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
        )


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
        )
        validators = [
            user_password,
        ]
