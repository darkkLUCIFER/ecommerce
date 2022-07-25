from django.db import models
from django.db.models import Q

from product_category.models import ProductCategory


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
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')

    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductGallery(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    image = models.ImageField(upload_to='gallery/', verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image', verbose_name='محصول')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'galleries'
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصویر ها'
