from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    slug = models.SlugField(max_length=120, unique_for_date='created', verbose_name='اسلاگ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product_categories'
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
