# Generated by Django 3.1 on 2021-09-01 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('company_name', models.CharField(max_length=128, unique=True)),
                ('registration_id', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModelHolder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gltf_url', models.URLField(max_length=1024)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
