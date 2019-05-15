# Generated by Django 2.0.2 on 2019-05-13 07:54

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60, verbose_name='Имя')),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='Почта')),
                ('password_hash', models.BigIntegerField(default=0, verbose_name='Хэш пароля')),
                ('description', models.TextField(default='', max_length=400, verbose_name='Описание')),
                ('liked_ids', models.CharField(default='', max_length=999999999, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Пролайканные айди')),
                ('paired_ids', models.CharField(default='', max_length=999999999, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Парные айди')),
                ('banned_ids', models.CharField(default='', max_length=999999999, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Забаненные айди')),
                ('profile_image', models.ImageField(upload_to='', verbose_name='Фото профиля')),
                ('sex', models.CharField(default='TRAP', max_length=10, verbose_name='Пол')),
                ('age', models.IntegerField(default=0, verbose_name='Возраст')),
                ('looking_age_from', models.IntegerField(default=18, verbose_name='Возраст поиска нижний')),
                ('lookin_age_to', models.IntegerField(default=99, verbose_name='Возраст поиска верхний')),
                ('looking_sex', models.CharField(default='TRAP', max_length=10, verbose_name='Пол поиска')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]