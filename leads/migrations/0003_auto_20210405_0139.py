# Generated by Django 3.1.7 on 2021-04-05 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210405_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='profile',
            new_name='organisation',
        ),
    ]