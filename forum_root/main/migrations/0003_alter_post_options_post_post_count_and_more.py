# Generated by Django 4.0.4 on 2022-04-25 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_section_options_alter_thread_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AddField(
            model_name='post',
            name='post_count',
            field=models.IntegerField(default=3, verbose_name='Количество сообщений'),
        ),
        migrations.AddField(
            model_name='thread',
            name='thread_count',
            field=models.IntegerField(default=2, verbose_name='Кол-во сообщений'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tread_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread', to='main.thread', verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='main.section', verbose_name='Раздел'),
        ),
    ]