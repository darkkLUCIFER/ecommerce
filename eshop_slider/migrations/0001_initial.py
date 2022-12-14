# Generated by Django 4.0.6 on 2022-07-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('link', models.URLField(max_length=100, verbose_name='آدرس')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider/', verbose_name='تصویر')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
                'db_table': 'sliders',
            },
        ),
    ]
