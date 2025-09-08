from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', null=True, blank=True, verbose_name='آواتار', )
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل')
    nationality = models.CharField(max_length=100, null=True, blank=True, verbose_name="ملیت")
    nationality_code = models.IntegerField(null=True, verbose_name='کد ملی')
    province = models.CharField(max_length=100, null=True, blank=True, verbose_name="استان")
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="شهر")

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.email



