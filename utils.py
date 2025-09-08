from django.core.mail import send_mail
from django.conf import settings


def send_activation_email(user):
    subject = "فعال‌سازی حساب کاربری"
    activation_link = f"http://127.0.0.1:8000/activate/{user.email_active_code}/"
    message = f"سلام {user.username or user.email},\n\nبرای فعال‌سازی حسابت روی لینک زیر کلیک کن:\n{activation_link}"

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

