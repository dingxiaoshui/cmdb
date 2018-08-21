# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-21 10:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('power', models.CharField(max_length=20, verbose_name='权限')),
            ],
            options={
                'db_table': 'cabinet',
            },
        ),
        migrations.CreateModel(
            name='hostinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255, verbose_name='主机名')),
                ('IP', models.CharField(max_length=50, verbose_name='IP地址')),
                ('Mem', models.IntegerField(verbose_name='内存')),
                ('CPU', models.CharField(max_length=255, verbose_name='cpu')),
                ('CPUS', models.IntegerField(verbose_name='cpus')),
                ('OS', models.CharField(max_length=255, verbose_name='os')),
                ('virtual1', models.CharField(max_length=255, verbose_name='virtual')),
                ('status', models.CharField(max_length=50, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='monitorMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostid', models.IntegerField(verbose_name='监控主机ID')),
                ('avai', models.CharField(max_length=20, verbose_name='空闲内存')),
                ('total', models.CharField(max_length=20, verbose_name='总内存')),
                ('ratio', models.CharField(max_length=20, verbose_name='使用率')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20, verbose_name='服务名称')),
                ('pid', models.IntegerField(verbose_name='pid')),
                ('module_letter', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='webserver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='手机')),
                ('user_role', models.CharField(max_length=40, verbose_name='角色')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
    ]
