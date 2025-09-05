from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', verbose_name='آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    groups = models.ManyToManyField(
        Group,
        verbose_name='گروه‌ها',
        blank=True,
        related_name='custom_user_set'  # اضافه شد
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='مجوزها',
        blank=True,
        related_name='custom_user_permissions_set'  # اضافه شد
    )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.email

