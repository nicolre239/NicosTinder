# Generated by Django 2.0.2 on 2019-05-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_user_lookin_age_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='looking_age_from',
            field=models.IntegerField(default=18, verbose_name='Возраст поиска нижний'),
        ),
    ]
