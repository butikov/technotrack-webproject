# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 20:32
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Имя события')),
                ('description', models.TextField(default='')),
                ('max_participants', models.IntegerField(default=-1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('location', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own_events',
                                             to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='events', to='core.Category')),
                ('participants',
                 models.ManyToManyField(related_name='participated_events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
    ]
