# Generated by Django 2.0.2 on 2019-05-13 17:55

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20190513_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='banned_ids',
            field=models.CharField(blank=True, default='', max_length=999999999, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Забаненные айди'),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, default='', max_length=400, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='user',
            name='liked_ids',
            field=models.CharField(blank=True, default='', max_length=999999999, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Пролайканные айди'),
        ),
        migrations.AlterField(
            model_name='user',
            name='paired_ids',
            field=models.CharField(blank=True, default='', max_length=999999999, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Парные айди'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='../static/images/no_image.png', null=True, upload_to='', verbose_name='Фото профиля'),
        ),
    ]
