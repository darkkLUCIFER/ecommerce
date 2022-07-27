# Generated by Django 4.0.6 on 2022-07-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=150, verbose_name='عنوان سایت')),
                ('address', models.CharField(max_length=400, verbose_name='آدرس')),
                ('phone', models.CharField(max_length=30, verbose_name='تلفن')),
                ('mobile', models.CharField(max_length=30, verbose_name='تلفن همراه')),
                ('fax', models.CharField(max_length=50, verbose_name='فکس')),
                ('email_address', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('about_us', models.TextField(verbose_name='درباره ما')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'مدیریت تنظیمات',
                'db_table': 'site_settings',
            },
        ),
    ]