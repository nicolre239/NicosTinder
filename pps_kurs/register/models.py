from django.db import models
from django.core.validators import *

class User(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=25, default="")
    email = models.EmailField(verbose_name="Почта", unique=True, default="")
    password_hash = models.BigIntegerField(verbose_name="Хэш пароля", default=0)
    description = models.TextField(verbose_name="Описание", max_length=400, default="", blank=True, null=True,)
    liked_ids = models.CharField(validators=[validate_comma_separated_integer_list], verbose_name="Пролайканные айди", default=None, max_length=999999999, blank=True, null=True,)
    paired_ids = models.CharField(validators=[validate_comma_separated_integer_list], verbose_name="Парные айди", default=None, max_length=999999999, blank=True, null=True,)
    banned_ids = models.CharField(validators=[validate_comma_separated_integer_list], verbose_name="Забаненные айди", default=None, max_length=999999999, blank=True, null=True,)
    profile_image = models.ImageField(verbose_name="Фото профиля", default="../static/images/no_image.png", blank=True, null=True,)
    sex = models.CharField(verbose_name="Пол", default="TRAP", max_length=10)
    age = models.IntegerField(verbose_name="Возраст", default=0)
    looking_age_from = models.IntegerField(verbose_name="Возраст поиска нижний", default=18)
    lookin_age_to = models.IntegerField(verbose_name="Возраст поиска верхний", default=99)
    looking_sex = models.CharField(verbose_name="Пол поиска", default="TRAP", max_length=10)

    def __str__(self):
        return "ID: %s %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
