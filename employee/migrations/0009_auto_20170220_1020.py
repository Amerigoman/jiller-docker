# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 10:20
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20170218_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuelog',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
    ]