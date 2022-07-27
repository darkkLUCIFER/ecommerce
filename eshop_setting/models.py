from django.db import models


class SiteSetting(models.Model):
    site_title = models.CharField(max_length=150, verbose_name='عنوان سایت')
    address = models.CharField(max_length=400, verbose_name='آدرس')
    phone = models.CharField(max_length=30, verbose_name='تلفن')
    mobile = models.CharField(max_length=30, verbose_name='تلفن همراه')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email_address = models.EmailField(max_length=50, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ما')
    copy_right = models.CharField(max_length=200, verbose_name='متن کپی رایت')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_title

    class Meta:
        db_table = 'site_settings'
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'
