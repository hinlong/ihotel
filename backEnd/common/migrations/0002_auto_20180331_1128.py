# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-31 11:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('current_status', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('check_in_date', models.DateTimeField()),
                ('expired_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Record',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('floor', models.IntegerField()),
                ('pattern', models.BooleanField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('people_counts', models.IntegerField(default=0)),
                ('expired_time', models.DateTimeField(blank=True, null=True)),
                ('last_nobody_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ues_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Room',
            },
        ),
        migrations.AddField(
            model_name='record',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room', to='common.Room'),
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userdetail', to=settings.AUTH_USER_MODEL),
        ),
    ]