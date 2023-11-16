from django.conf import settings
from django.db import models


from users.models import User

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    """
        Модель представляет курс в онлайн школе.

        Attributes:
            title (str): Название курса (максимум 50 символов).
            preview (ImageField): Превью курса, изображение.
            description (str): Описание курса.

        Methods:
            __str__(): Возвращает строковое представление объекта, используется для отображения
                названия курса при выводе в административной панели Django.
    """
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', null=True)
    description = models.TextField(verbose_name='описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'



class Lesson(models.Model):
    """
        Модель представляет урок в онлайн школе.

        Attributes:
            title (str): Название урока (максимум 150 символов).
            description (str): Описание урока.
            preview (ImageField): Превью урока, изображение.
            url (URLField): Ссылка на видеоурок.

        Relationships:
            course (ForeignKey): Внешний ключ, связывающий урок с курсом.
                Урок привязан к одному курсу, курс может содержать много уроков.

        Methods:
            __str__(): Возвращает строковое представление объекта, используется для отображения
                названия урока при выводе в административной панели Django.
    """
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', null=True)
    url = models.URLField(verbose_name='ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")

    def __str__(self):
        return f'{self.title}'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    date = models.DateTimeField(verbose_name='дата оплаты', **NULLABLE)
    course = models.ForeignKey(Course, verbose_name='оплаченный курс', related_name='payment',
                               on_delete=models.CASCADE, **NULLABLE)
    lesson = models.ForeignKey(Lesson, verbose_name='оплаченный урок', related_name='payment',
                               on_delete=models.CASCADE,**NULLABLE)
    total = models.FloatField(verbose_name='сумма оплаты', **NULLABLE)

    payment_mode = [
        ('наличные', 'Наличные'),
        ('перевод на счет', 'Перевод на счет'),
    ]
    payment_choice = models.CharField(max_length=50, choices=payment_mode,
                                      verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user}, {self.total}: {self.lesson if self.lesson else self.course}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

        ordering = ('date',)


class Subscription(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f'{self.user.email} - {self.course.title}'