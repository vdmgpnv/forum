from msilib.schema import LockPermissions
import time
from django.db import models

from app_users.models import AdvUser

class Section(models.Model):
    section_name = models.CharField(max_length=30, unique=True, verbose_name='Раздел')
    
    def __str__(self) -> str:
        return self.section_name
    
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
    
class Thread(models.Model):
    thread_name = models.CharField(max_length=100, verbose_name='Тема')
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section', verbose_name='Раздел')
    thread_count = models.IntegerField(verbose_name='Кол-во сообщений', default=2)    
    
    def __str__(self) -> str:
        return self.thread_name
    
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
    
    
class Post(models.Model):
    tread_id = models.ForeignKey(Thread, null=True, on_delete=models.CASCADE, related_name='thread', verbose_name='Тема')
    user_id = models.ForeignKey(AdvUser, null=False, on_delete=models.CASCADE, related_name='user', verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    post_count = models.IntegerField(verbose_name='Количество сообщений', default=3)
    text = models.TextField(max_length=500, verbose_name='Текст сообщения')
    
    def show_post(self):
        return self.text[0:100] + '...'
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
    
    def __str__(self) -> str:
        return self.text[:10] + '...'