# Generated by Django 4.0.4 on 2022-05-17 12:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_thread_section_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(max_length=1000, verbose_name='Текст сообщения'),
        ),
    ]
