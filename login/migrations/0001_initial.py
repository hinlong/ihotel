# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-22 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('avatar', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('access_token', models.CharField(blank=True, max_length=100)),
                ('refresh_token', models.CharField(blank=True, max_length=100)),
                ('expires_in', models.BigIntegerField(default=0, max_length=100)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
