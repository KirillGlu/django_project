from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
        Расширенная модель пользователя для проекта Django.

        Заменяет стандартную модель пользователя Django для включения
        дополнительной информации, такой как email, аватар, телефон и страна.

        Attributes:
            email (str): Уникальный адрес электронной почты пользователя.
            avatar (ImageField): Изображение профиля пользователя.
            phone (str): Номер телефона пользователя.
            country (str): Страна, в которой проживает пользователь.
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='Аватар')
    phone = models.CharField(max_length=35, verbose_name='Телефон')
    country = models.CharField(max_length=35, verbose_name='Страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []