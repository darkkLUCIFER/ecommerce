from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    link = models.URLField(max_length=100, verbose_name='آدرس')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(null=True, blank=True, upload_to='slider/', verbose_name='تصویر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'sliders'
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'
