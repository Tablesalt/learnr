# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 09:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learnrapp', '0003_auto_20161015_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=4000, null=True)),
                ('output', models.CharField(max_length=4000, null=True)),
                ('last_watched', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]