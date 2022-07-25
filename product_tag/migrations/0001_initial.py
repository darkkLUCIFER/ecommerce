# Generated by Django 4.0.6 on 2022-07-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_product_options_alter_product_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=250, unique_for_date='created', verbose_name='اسلاگ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('active', models.BooleanField(default=True, verbose_name='فعال')),
                ('products', models.ManyToManyField(blank=True, to='product.product', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
                'db_table': 'tags',
            },
        ),
    ]