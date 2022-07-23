from django.db import models
from django.db.models import Q


class ProductManager(models.Manager):
    def search(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    image = models.ImageField(null=True, blank=True, upload_to='products/', verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال')

    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
