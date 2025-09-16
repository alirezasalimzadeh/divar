from django.db import models

IRAN_CITIES = [
    ('abadan', 'آبادان'),
    ('abadeh', 'آباده'),
    ('abyek', 'آبیک'),
    ('ahvaz', 'اهواز'),
    ('ajabshir', 'عجب‌شیر'),
    ('arak', 'اراک'),
    ('ardabil', 'اردبیل'),
    ('arsanjan', 'ارسنجان'),
    ('asaluyeh', 'عسلویه'),
    ('azarshahr', 'آذرشهر'),
    ('babolsar', 'بابلسر'),
    ('bandarabbas', 'بندرعباس'),
    ('bandarlengeh', 'بندرلنگه'),
    ('bojnurd', 'بجنورد'),
    ('borujerd', 'بروجرد'),
    ('bushehr', 'بوشهر'),
    ('birjand', 'بیرجند'),
    ('bukan', 'بوکان'),
    ('chabahar', 'چابهار'),
    ('damghan', 'دامغان'),
    ('dezful', 'دزفول'),
    ('divandarreh', 'دیواندره'),
    ('esfarayen', 'اسفراین'),
    ('fasa', 'فسا'),
    ('gorgan', 'گرگان'),
    ('hamadan', 'همدان'),
    ('ilam', 'ایلام'),
    ('iranshahr', 'ایرانشهر'),
    ('isfahan', 'اصفهان'),
    ('jahrom', 'جهرم'),
    ('jiroft', 'جیرفت'),
    ('karaj', 'کرج'),
    ('kashan', 'کاشان'),
    ('kerman', 'کرمان'),
    ('kermanshah', 'کرمانشاه'),
    ('khorramabad', 'خرم‌آباد'),
    ('khoy', 'خوی'),
    ('lahijan', 'لاهیجان'),
    ('maragheh', 'مراغه'),
    ('marvdasht', 'مرودشت'),
    ('mashhad', 'مشهد'),
    ('miandoab', 'میاندوآب'),
    ('minab', 'میناب'),
    ('najafabad', 'نجف‌آباد'),
    ('nishapur', 'نیشابور'),
    ('orumiyeh', 'ارومیه'),
    ('qazvin', 'قزوین'),
    ('qom', 'قم'),
    ('rasht', 'رشت'),
    ('sabzevar', 'سبزوار'),
    ('sanandaj', 'سنندج'),
    ('sari', 'ساری'),
    ('semnan', 'سمنان'),
    ('shahrekord', 'شهرکرد'),
    ('shiraz', 'شیراز'),
    ('tabriz', 'تبریز'),
    ('tehran', 'تهران'),
    ('yazd', 'یزد'),
    ('zanjan', 'زنجان'),
]


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته ها"

    def __str__(self):
        return self.name

    def get_full_path(self):
        path = [self]
        parent = self.parent
        while parent is not None:
            path.append(parent)
            parent = parent.parent
        return list(reversed(path))


class Ads(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(choices=IRAN_CITIES, max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = " آگهی"
        verbose_name_plural = "همه آگهی ‌ها"

    def __str__(self):
        return self.title


class RealEstateAd(Ads):
    area = models.PositiveIntegerField(verbose_name="متراژ (متر مربع)", null=True, blank=True)
    is_images_for_this_property = models.BooleanField(
        default=True,
        verbose_name="تصاویر مربوط به همین ملک است؟")
    price_per_meter = models.IntegerField(
        blank=True, null=True,
        verbose_name="قیمت هر متر")

    FLOOR_CHOICES = [
        (0, "همکف"),
        (-1, "زیرزمین"),
        (1, "طبقه 1"),
        (2, "طبقه 2"),
        (3, "طبقه 3"),
        (4, "طبقه 4"),
        (5, "طبقه 5 و بالاتر"),
    ]
    floor = models.IntegerField(
        choices=FLOOR_CHOICES,
        blank=True, null=True,
        verbose_name="طبقه"
    )

    has_elevator = models.BooleanField(default=False, verbose_name="آسانسور")
    has_parking = models.BooleanField(default=False, verbose_name="پارکینگ")
    has_storage = models.BooleanField(default=False, verbose_name="انباری")

    class Meta:
        verbose_name = "آگهی املاک"
        verbose_name_plural = "آگهی‌های املاک"

    def __str__(self):
        return f"{self.title} - {self.city}"


class CarAd(Ads):
    mileage = models.PositiveIntegerField(verbose_name="کارکرد (کیلومتر)", help_text="میزان کارکرد خودرو به کیلومتر",
                                          null=True, blank=True)

    production_year = models.PositiveSmallIntegerField(verbose_name="سال تولید", null=True, blank=True)

    color = models.CharField(max_length=30, verbose_name="رنگ", null=True, blank=True)

    brand = models.CharField(max_length=50, verbose_name="برند", null=True, blank=True)

    model = models.CharField(max_length=50, verbose_name="مدل", null=True, blank=True)

    trim = models.CharField(max_length=50, verbose_name="تیپ", null=True, blank=True)

    insurance_expiry = models.DateField(verbose_name="مهلت بیمه شخص ثالث", null=True, blank=True)

    GEARBOX_CHOICES = [
        ('manual', 'دنده‌ای'),
        ('automatic', 'اتوماتیک'),
    ]
    gearbox = models.CharField(max_length=10, choices=GEARBOX_CHOICES, verbose_name="گیربکس")

    FUEL_CHOICES = [
        ('gasoline', 'بنزین'),
        ('diesel', 'دیزل'),
        ('cng', 'گاز CNG'),
        ('hybrid', 'هیبرید'),
        ('electric', 'برقی'),
    ]
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES, verbose_name="نوع سوخت")

    class Meta:
        verbose_name = "آگهی خودرو"
        verbose_name_plural = "آگهی‌های خودرو"

    def __str__(self):
        return f"{self.brand} {self.trim} - {self.production_year}"


class DigitalProductAd(Ads):
    brand = models.CharField(max_length=50, verbose_name="برند")

    model_name = models.CharField(max_length=100, verbose_name="مدل دستگاه")

    CONDITION_CHOICES = [
        ('new', 'نو'),
        ('used', 'کارکرده'),
        ('refurbished', 'بازسازی‌شده'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, verbose_name="وضعیت کالا")

    storage_capacity = models.PositiveIntegerField(blank=True, null=True, verbose_name="حافظه داخلی (GB)")

    color = models.CharField(max_length=30, blank=True, null=True, verbose_name="رنگ")

    operating_system = models.CharField(max_length=50, blank=True, null=True, verbose_name="سیستم‌عامل")

    warranty = models.BooleanField(default=False, verbose_name="دارای گارانتی")

    warranty_period = models.PositiveIntegerField(blank=True, null=True, verbose_name="مدت گارانتی (ماه)")

    class Meta:
        verbose_name = "آگهی کالای دیجیتال"
        verbose_name_plural = "آگهی‌های کالای دیجیتال"

    def __str__(self):
        return f"{self.brand} {self.model_name} - {self.condition}"


class HomeKitchenAd(Ads):
    brand = models.CharField(max_length=50, verbose_name="برند")

    material = models.CharField(max_length=50, verbose_name="جنس")

    product_type = models.CharField(max_length=100, verbose_name="نوع محصول")

    CONDITION_CHOICES = [
        ('new', 'نو'),
        ('used', 'کارکرده'),
    ]
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, verbose_name="وضعیت کالا")

    color = models.CharField(max_length=30, blank=True, null=True, verbose_name="رنگ")

    dimensions = models.CharField(max_length=100, blank=True, null=True, verbose_name="ابعاد / وزن")

    class Meta:
        verbose_name = "آگهی خانه و آشپزخانه"
        verbose_name_plural = "آگهی‌های خانه و آشپزخانه"

    def __str__(self):
        return f"{self.product_type} - {self.brand}"


class ServiceAd(Ads):
    service_type = models.CharField(max_length=100, verbose_name="نوع خدمت")

    experience_years = models.PositiveIntegerField(verbose_name="سابقه کار (سال)")

    service_location = models.CharField(max_length=100, blank=True, null=True, verbose_name="محل ارائه خدمت")

    is_remote = models.BooleanField(default=False, verbose_name="امکان ارائه غیرحضوری")

    details = models.TextField(blank=True, null=True, verbose_name="توضیحات تکمیلی")

    class Meta:
        verbose_name = "آگهی خدمات"
        verbose_name_plural = "آگهی‌های خدمات"

    def __str__(self):
        return f"{self.service_type} - {self.experience_years} سال سابقه"


class PersonalItemAd(Ads):
    CONDITION_CHOICES = [('new', 'نو'), ('used', 'کارکرده')]
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, verbose_name="وضعیت کالا")
    item_type = models.CharField(max_length=50, verbose_name="نوع کالا")
    brand = models.CharField(max_length=50, blank=True, null=True, verbose_name="برند")
    material = models.CharField(max_length=50, blank=True, null=True, verbose_name="جنس")
    color = models.CharField(max_length=30, blank=True, null=True, verbose_name="رنگ")

    class Meta:
        verbose_name = "آگهی وسایل شخصی"
        verbose_name_plural = "آگهی‌های وسایل شخصی"

    def __str__(self):
        return f"{self.item_type} - {self.condition}"


class EntertainmentAd(Ads):
    ENTERTAINMENT_TYPE_CHOICES = [
        ('event', 'رویداد'),
        ('instrument', 'ساز موسیقی'),
        ('sport', 'لوازم ورزشی'),
        ('game', 'بازی'),
        ('other', 'سایر')
    ]
    CONDITION_CHOICES = [
        ('new', 'نو'),
        ('used', 'کارکرده')
    ]
    entertainment_type = models.CharField(max_length=20, choices=ENTERTAINMENT_TYPE_CHOICES, verbose_name="نوع سرگرمی")
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, verbose_name="وضعیت")
    brand = models.CharField(max_length=50, blank=True, null=True, verbose_name="برند")
    genre = models.CharField(max_length=50, blank=True, null=True, verbose_name="ژانر / دسته‌بندی")
    event_date = models.DateField(blank=True, null=True, verbose_name="تاریخ برگزاری")

    class Meta:
        verbose_name = "آگهی سرگرمی و فراغت"
        verbose_name_plural = "آگهی‌های سرگرمی و فراغت"

    def __str__(self):
        return f"{self.entertainment_type} - {self.title}"


class IndustrialEquipmentAd(Ads):
    equipment_type = models.CharField(max_length=100, verbose_name="نوع تجهیزات")
    power = models.CharField(max_length=50, verbose_name="توان / قدرت", null=True, blank=True)
    brand = models.CharField(max_length=50, blank=True, null=True, verbose_name="برند")
    condition = models.CharField(max_length=20, choices=[('new', 'نو'), ('used', 'کارکرده')], verbose_name="وضعیت")
    manufacture_year = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="سال ساخت")

    class Meta:
        verbose_name = "آگهی تجهیزات و صنعتی"
        verbose_name_plural = "آگهی‌های تجهیزات و صنعتی"

    def __str__(self):
        return f"{self.equipment_type} - {self.brand if self.brand else ''}"


class JobListingAd(Ads):
    position = models.CharField(max_length=100, verbose_name="عنوان شغلی")
    company = models.CharField(max_length=100, verbose_name="نام شرکت")
    location = models.CharField(max_length=100, verbose_name="محل کار")
    employment_type = models.CharField(max_length=20, choices=[
        ('full_time', 'تمام وقت'),
        ('part_time', 'پاره وقت'),
        ('remote', 'دورکاری'),
        ('contract', 'قراردادی')
    ],verbose_name="نوع همکاری")
    salary = models.IntegerField(blank=True, null=True, verbose_name="حقوق")
    experience_required = models.PositiveIntegerField(blank=True, null=True, verbose_name="سابقه کار مورد نیاز (سال)")
    education = models.CharField(max_length=100, blank=True, null=True, verbose_name="مدرک تحصیلی")

    class Meta:
        verbose_name = "آگهی استخدام"
        verbose_name_plural = "آگهی‌های استخدام"

    def __str__(self):
        return f"{self.position} - {self.company}"


class AdImage(models.Model):
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='ads_images/')
    alt_text = models.CharField(max_length=150, blank=True, null=True, verbose_name="توضیح تصویر")

    class Meta:
        verbose_name = "تصویر آگهی"
        verbose_name_plural = "تصاویر آگهی‌ها"

    def __str__(self):
        return f"تصویر {self.ad.title}"


