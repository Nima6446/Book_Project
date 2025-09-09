from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView, TokenBlacklistView

from . import views
from .views import ActivateUserView, MyTokenObtainPairView, ForgetPasswordView, ResetPasswordView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('activate/<str:code>/', ActivateUserView.as_view(), name="activate_page"),
    path('api/login/', MyTokenObtainPairView.as_view(), name='login_page'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_page'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify_page'),
    path('api/logout/', LogoutView.as_view(), name='logout_page'),
    path("forget-password/", ForgetPasswordView.as_view(), name="forget_password"),
    path("reset-password/<str:code>/", ResetPasswordView.as_view(), name="reset_password"),
]

