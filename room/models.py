from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from account.models import User


class Property(models.Model):
    ROOM = "room"
    VILLA = "villa"
    PRODUCT_TYPES = [
        (ROOM, "اتاق"),
        (VILLA, "ویلا"),
    ]
    name = models.CharField(max_length=100, db_index=True,verbose_name="نام هتل/ویلا")
    slug = models.SlugField(max_length=150, db_index=True, unique=True,verbose_name="نام در URL")
    type = models.CharField(max_length=20, db_index=True, choices=PRODUCT_TYPES, verbose_name="نوع اقامتگاه")
    rating = models.CharField(validators=[MinValueValidator(1), MaxValueValidator(5)],null=True, blank=True,verbose_name="امتیاز")
    owner = models.ForeignKey(User, on_delete=models.CASCADE,db_index=True,verbose_name="میزبان")
    country = models.CharField(max_length=100,db_index=True,verbose_name="کشور")
    province = models.CharField(max_length=10,verbose_name="استان")
    city = models.CharField(max_length=100, db_index=True,verbose_name="شهر")
    address = models.CharField(max_length=200,blank=True,verbose_name="آدرس")
    tell = models.CharField(max_length=20,blank=True,verbose_name="تلفن")
    email = models.EmailField(max_length=100,blank=True,verbose_name="ایمیل")
    email = models.EmailField(max_length=100,blank=True,verbose_name="ایمیل")


