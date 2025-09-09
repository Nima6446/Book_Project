from django.utils.crypto import get_random_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
        #todo : activation validating
        return user

    from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
    from rest_framework import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
        # اضافه کردن فیلدهای دلخواه به خروجی توکن
        def validate(self, attrs):
            data = super().validate(attrs)  # این چک username/password رو انجام میده
            user = self.user

            # مثال: جلوگیری از لاگین اگر ایمیل فعال نشده
            if not user.is_active:
                raise serializers.ValidationError("اکانت فعال نیست. ایمیل را تأیید کنید.")

            # اضافه کردن info کاربر به response
            data.update({
                'user_id': user.id,
                'email': user.email,
                'username': user.get_username(),
            })
            return data

