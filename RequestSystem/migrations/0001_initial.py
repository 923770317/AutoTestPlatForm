# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-10 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u6a21\u5757')),
                ('logic_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u63a5\u53e3\u540d')),
                ('protocol_type', models.CharField(max_length=10, verbose_name='\u534f\u8bae\u7c7b\u578b')),
                ('method', models.CharField(max_length=20, verbose_name='\u8bf7\u6c42\u65b9\u6cd5')),
                ('url', models.CharField(max_length=100, verbose_name='\u8bf7\u6c42\u5730\u5740')),
                ('headers', models.CharField(blank=True, max_length=300, null=True, verbose_name='\u8bf7\u6c42\u5934')),
                ('request_body', models.CharField(blank=True, max_length=500, null=True, verbose_name='\u8bf7\u6c42\u4f53')),
                ('is_ci', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6301\u7eed\u96c6\u6210')),
                ('logic_delete', models.BooleanField(default=False)),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RequestSystem.Models')),
            ],
        ),
        migrations.CreateModel(
            name='Systems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u7cfb\u7edf')),
                ('logic_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='models',
            name='system_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RequestSystem.Systems'),
        ),
    ]
