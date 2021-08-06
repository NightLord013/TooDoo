from django.db import models
from UserApp.models import User
from django.utils import timezone
from django.contrib.sessions.models import Session

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category', verbose_name='Пользователь')
    name = models.CharField(max_length=30, verbose_name='Название категории')
    color = models.CharField(max_length=7, blank=True, null=True, verbose_name='Цвет')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.name

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_note', verbose_name='Пользователь')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    #text = models.TextField(verbose_name='Текст')
    deadline = models.DateTimeField(blank=True, null=True, default=timezone.datetime.now().replace(microsecond=0), verbose_name='Дата и время выполнения')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')

    class Meta:
        ordering = ['category', 'deadline', ]
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title


# class UserSession(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     session = models.ForeignKey(Session, on_delete=models.CASCADE)



