from django.utils.crypto import get_random_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from account.models import User
from utils import send_activation_email


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = 'username', 'email', 'password'

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            is_active = False
        )
        user.email_active_code = get_random_string(72)
        user.set_password(validated_data['password'])  # هش کردن پسورد
        user.save()
        send_activation_email(user)
        return user
