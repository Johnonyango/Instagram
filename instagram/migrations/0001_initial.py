# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-02 12:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='articles/')),
                ('image_name', models.CharField(max_length=30)),
                ('image_caption', tinymce.models.HTMLField()),
                ('likes', models.CharField(max_length=50)),
                ('comments', models.CharField(max_length=50)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, upload_to='articles')),
                ('bio', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=30)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]
