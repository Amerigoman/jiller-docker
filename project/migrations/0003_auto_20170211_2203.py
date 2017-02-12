# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170207_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.CharField(choices=[('User story', 'User story'), ('Task', 'Task'), ('Bug', 'Bug')], default='Task', max_length=255, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='new', max_length=255, verbose_name='Status'),
        ),
    ]
