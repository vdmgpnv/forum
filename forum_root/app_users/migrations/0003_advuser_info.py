# Generated by Django 4.0.4 on 2022-05-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_remove_advuser_send_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='info',
            field=models.TextField(null=True),
        ),
    ]
