# Generated by Django 2.0.2 on 2019-05-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='../static/images/no_image.png', upload_to='', verbose_name='Фото профиля'),
        ),
    ]
