from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


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

