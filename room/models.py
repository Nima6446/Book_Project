from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Property(models.Model):
    countries = [
        "افغانستان",
        "آلبانی",
        "الجزایر",
        "آندورا",
        "آنگولا",
        "آنتیگوا و باربودا",
        "آرژانتین",
        "ارمنستان",
        "استرالیا",
        "اتریش",
        "آذربایجان",
        "باهاما",
        "بحرین",
        "بنگلادش",
        "باربادوس",
        "بلاروس",
        "بلژیک",
        "بلیز",
        "بنین",
        "بوتان",
        "بولیوی",
        "بوسنی و هرزگوین",
        "بوتسوانا",
        "برزیل",
        "برونئی",
        "بلغارستان",
        "بورکینافاسو",
        "بوروندی",
        "کاپ ورد",
        "کامبوج",
        "کامرون",
        "کانادا",
        "جمهوری آفریقای مرکزی",
        "چاد",
        "شیلی",
        "چین",
        "کلمبیا",
        "کومور",
        "کنگو (جمهوری)",
        "کنگو (جمهوری دموکراتیک)",
        "کاستاریکا",
        "کرواسی",
        "کوبا",
        "قبرس",
        "چک",
        "دانمارک",
        "جیبوتی",
        "دومینیکا",
        "جمهوری دومینیکن",
        "اکوادور",
        "مصر",
        "السالوادور",
        "استونی",
        "اسواتینی",
        "اتیوپی",
        "فیجی",
        "فنلاند",
        "فرانسه",
        "گابن",
        "گامبیا",
        "گرجستان",
        "آلمان",
        "غنا",
        "یونان",
        "گرانادا",
        "گواتمالا",
        "گینه",
        "گینه بیسائو",
        "گویان",
        "هائیتی",
        "هندوراس",
        "مجارستان",
        "ایسلند",
        "هند",
        "اندونزی",
        "ایران",
        "عراق",
        "ایرلند",
        "اسرائیل",
        "ایتالیا",
        "جامائیکا",
        "ژاپن",
        "اردن",
        "قزاقستان",
        "کنیا",
        "کیریباتی",
        "کویت",
        "قرقیزستان",
        "لائوس",
        "لتونی",
        "لبنان",
        "لسوتو",
        "لیبریا",
        "لیبی",
        "لیختن‌اشتاین",
        "لیتوانی",
        "لوکزامبورگ",
        "ماداگاسکار",
        "مالاوی",
        "مالزی",
        "مالدیو",
        "مالی",
        "مالت",
        "جزایر مارشال",
        "موریتانی",
        "موریس",
        "مکزیک",
        "میکرونزی",
        "مولداوی",
        "موناکو",
        "مغولستان",
        "مونته‌نگرو",
        "مراکش",
        "موزامبیک",
        "میانمار",
        "نامیبیا",
        "نائورو",
        "نپال",
        "هلند",
        "نیوزیلند",
        "نیکاراگوئه",
        "نیجر",
        "نیجریه",
        "کره شمالی",
        "مقدونیه شمالی",
        "نروژ",
        "عمان",
        "پاکستان",
        "پالائو",
        "فلسطین",
        "پاناما",
        "پاپوآ گینه نو",
        "پاراگوئه",
        "پرو",
        "فیلیپین",
        "لهستان",
        "پرتغال",
        "قطر",
        "رومانی",
        "روسیه",
        "رواندا",
        "سنت کیتس و نویس",
        "سنت لوسیا",
        "سنت وینسنت و گرنادین‌ها",
        "ساموآ",
        "سان مارینو",
        "سائوتومه و پرنسیپ",
        "عربستان سعودی",
        "سنگال",
        "صربستان",
        "سیشل",
        "سیرالئون",
        "سنگاپور",
        "اسلواکی",
        "اسلوونی",
        "جزایر سلیمان",
        "سومالی",
        "آفریقای جنوبی",
        "کره جنوبی",
        "اسپانیا",
        "سریلانکا",
        "سودان",
        "سودان جنوبی",
        "سورینام",
        "سوئد",
        "سوئیس",
        "سوریه",
        "تاجیکستان",
        "تانزانیا",
        "تایلند",
        "تیمور شرقی",
        "توگو",
        "تونگا",
        "ترینیداد و توباگو",
        "تونس",
        "ترکیه",
        "ترکمنستان",
        "تووالو",
        "اوگاندا",
        "اوکراین",
        "امارات متحده عربی",
        "بریتانیا",
        "ایالات متحده آمریکا",
        "اروگوئه",
        "ازبکستان",
        "وانواتو",
        "واتیکان",
        "ونزوئلا",
        "ویتنام",
        "یمن",
        "زامبیا",
        "زیمبابوه",
    ]
    ROOM = "room"
    VILLA = "villa"
    PRODUCT_TYPES = [
        (ROOM, "اتاق"),
        (VILLA, "ویلا"),
    ]
    hotel_name = models.CharField(max_length=100, db_index=True, verbose_name="نام هتل/ویلا")
    type = models.CharField(max_length=20, db_index=True, choices=PRODUCT_TYPES, verbose_name="نوع اقامتگاه")
    country = models.CharField(max_length=100, choices=[(c, c) for c in countries], db_index=True, verbose_name="کشور")
    province = models.CharField(max_length=100, verbose_name="استان")
    city = models.CharField(max_length=100, db_index=True, verbose_name="شهر")
    address = models.CharField(max_length=200, blank=True, verbose_name="آدرس")
    tell = models.CharField(max_length=20, blank=True, verbose_name="تلفن")
    email = models.EmailField(max_length=100, blank=True, verbose_name="ایمیل")
    default_checkin_time = models.TimeField(null=True, blank=True, verbose_name="زمان تحویل به میهمان")
    default_checkout_time = models.TimeField(null=True, blank=True, verbose_name="زمان تحویل به میزبان")

    class Meta:
        verbose_name = 'هتل'
        verbose_name_plural = 'هتل ها'
        constraints = [
            models.UniqueConstraint(fields=["hotel_name", "city"], name="unique_name_city"),
        ]
        indexes = [
            models.Index(fields=["type", "city", "hotel_name"]),
        ]

    def __str__(self):
        return self.hotel_name


class Room(models.Model):
    hotel_name = models.ForeignKey(Property, db_index=True, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name="نام هتل")
    title = models.CharField(max_length=100, db_index=True, verbose_name="عنوان")
    slug = models.SlugField(max_length=150, db_index=True, unique=True, verbose_name="نام در URL")
    capacity = models.IntegerField(db_index=True, verbose_name="ظرفیت")
    number_of_room = models.IntegerField(db_index=True, verbose_name="تعداد اتاق")
    size = models.IntegerField(verbose_name="متراژ")
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True,
                                              blank=True, verbose_name="امتیاز")
    price = models.DecimalField(max_digits=12, decimal_places=2, db_index=True, verbose_name="قیمت اجاره")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    is_active = models.BooleanField(db_index=True, verbose_name="فعال/غیر فعال")
    amenity = models.TextField(null=True, blank=True, verbose_name="سرویس ها/امکانات")

    class Meta:
        verbose_name = 'اتاق'
        verbose_name_plural = 'اتاق ها'
        constraints = [
            models.UniqueConstraint(fields=["slug"], name="unique_property_slug"),
            models.UniqueConstraint(fields=["hotel_name", "title"], name="unique_room_in_hotel"),
            models.CheckConstraint(check=models.Q(rating__gte=1, rating__lte=5), name="valid_room_rating"),
        ]


    def __str__(self):
        return self.title


class Availability(models.Model):
    room = models.ForeignKey(Room, db_index=True, on_delete=models.CASCADE)
    date = models.DateField(db_index=True, verbose_name="تاریخ")
    units_total = models.PositiveSmallIntegerField(db_index=True, verbose_name="تعداد اتاق های خالی")
    units_reserves = models.PositiveSmallIntegerField(db_index=True, default=0, verbose_name="تعداد اتاق های رزرو شده")
    is_close = models.BooleanField(db_index=True, default=False, verbose_name="فروش بسته/باز")
    price_override = models.DecimalField(max_digits=12,decimal_places=2,null=True, blank=True, verbose_name="قیمت جایگزین")
    min_nights = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="حداقل شب قابل رزرو")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین بروزرسانی")

    class Meta:
        verbose_name = 'وضعیت اتاق'
        verbose_name_plural = 'وضعیت اتاق ها'
        constraints = [
            models.UniqueConstraint(fields=["room", "date"], name="unique_room_date"),
            models.CheckConstraint(check=models.Q(units_reserves__lte=models.F("units_total")),
                                   name="reserves_lte_total"),
        ]
        indexes = [
            models.Index(fields=["room", "date"]),
            models.Index(fields=["is_close"]),
        ]

    def __str__(self):
        return self.room.title
