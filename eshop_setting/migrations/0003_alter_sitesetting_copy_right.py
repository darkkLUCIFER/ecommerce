# Generated by Django 4.0.6 on 2022-07-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_setting', '0002_sitesetting_copy_right'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='copy_right',
            field=models.CharField(max_length=200, verbose_name='متن کپی رایت'),
        ),
    ]