from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AdvUser(AbstractUser):
    date_of_birth = models.DateField(null=True, verbose_name='Дата рождения')
    send_messages = models.BooleanField(default=True, verbose_name='Хотите получать уведомления о новых постах?')
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'