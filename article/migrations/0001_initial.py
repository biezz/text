# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-20 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('block', '0002_auto_20180720_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章名称')),
                ('content', models.CharField(max_length=10000, verbose_name='文章描述')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '删除')], verbose_name='状态')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='最近更新时间')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Block', verbose_name='板块ID')),
            ],
        ),
    ]
