# Generated by Django 3.1 on 2021-10-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210901_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelholder',
            name='search',
            field=models.CharField(default='', max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
