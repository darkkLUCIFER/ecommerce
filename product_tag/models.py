from django.db import models
from product.models import Product


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    slug = models.SlugField(max_length=250, unique_for_date='created', verbose_name='اسلاگ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    active = models.BooleanField(default=True, verbose_name='فعال')
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tags'
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'
