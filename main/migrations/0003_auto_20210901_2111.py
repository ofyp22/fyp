# Generated by Django 3.1 on 2021-09-01 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210901_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.AlterModelManagers(
            name='company',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='company',
            name='email',
        ),
        migrations.RemoveField(
            model_name='company',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='company',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='company',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='company',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='company',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='company',
            name='username',
        ),
    ]
