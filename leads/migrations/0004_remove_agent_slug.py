# Generated by Django 3.1.7 on 2021-05-22 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20210522_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='slug',
        ),
    ]
