# Generated by Django 3.1.7 on 2021-05-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='slug',
            field=models.SlugField(max_length=20, null=True),
        ),
    ]
