from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=40, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    site_logo = models.ImageField(upload_to="images/site_settings/", verbose_name='لوگو سایت')
    addres = models.CharField(max_length=200, verbose_name='آدرس')
    tell = models.CharField(max_length=20, verbose_name='تلفن')
    email = models.CharField(max_length=200, verbose_name='ایمیل')
    copy_right_text = models.CharField(max_length=400, verbose_name='متن کپی رایت')
    about_us_page = models.CharField(verbose_name='درباره ما')
    is_main_settings = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:

        verbose_name = 'تنظیمات سایت'
    verbose_name_plural = 'تنظیمات'


    def __str__(self):
        return self.site_name


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    descriptuon = models.TextField(max_length=200, verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/slider', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title
