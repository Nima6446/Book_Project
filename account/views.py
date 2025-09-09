from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from Book_Project import settings
from utils import set_reset_code
from .models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateUserView(APIView):
    def get(self, request, code):
        try:
            user = User.objects.get(activation_code=code)
            user.is_active = True
            user.email_active_code = None  # کد مصرف بشه
            user.save()
            return Response({"message": "حساب شما با موفقیت فعال شد ✅"})
        except User.DoesNotExist:
            return Response({"error": "کد فعال‌سازی معتبر نیست"}, status=400)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        # todo CSRF token Problem most be solve


class ForgetPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
            code = set_reset_code(user)

            reset_link = f"http://127.0.0.1:8000/reset-password/{code}/"
            send_mail(
                "Reset your password",
                f"برای ریست پسورد روی لینک کلیک کن: {reset_link}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
            return Response({"message": "لینک ریست به ایمیل ارسال شد"})
        except User.DoesNotExist:
            return Response({"error": "کاربر با این ایمیل پیدا نشد"}, status=404)


class ResetPasswordView(APIView):
    def post(self, request, code):
        password = request.data.get("password")
        try:
            user = User.objects.get(email_active_code=code)
            user.set_password(password)
            user.email_active_code = ""  # مصرف شد
            user.save()
            return Response({"message": "رمز عبور با موفقیت تغییر کرد"})
        except User.DoesNotExist:
            return Response({"error": "کد معتبر نیست"}, status=400)
