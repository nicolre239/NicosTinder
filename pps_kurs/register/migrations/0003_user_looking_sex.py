# Generated by Django 2.0.2 on 2019-05-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20190513_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='looking_sex',
            field=models.CharField(default='TRAP', max_length=10, verbose_name='Пол поиска'),
        ),
    ]