# Generated by Django 3.0.5 on 2021-09-03 19:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10, verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last name')),
                ('middle_name', models.CharField(blank=True, max_length=20, verbose_name='Middle name')),
                ('position', models.CharField(max_length=20, verbose_name='Position')),
                ('private_phone', models.CharField(blank=True, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+70123456789'.from 9 up to 15 digits allowed.", regex='^\\+\\d{9,15}$')], verbose_name='Private phone')),
                ('work_phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+70123456789'.from 9 up to 15 digits allowed.", regex='^\\+\\d{9,15}$')], verbose_name='Work phone')),
                ('fax', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+70123456789'.from 9 up to 15 digits allowed.", regex='^\\+\\d{9,15}$')], verbose_name='Fax')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Title')),
                ('address', models.TextField(blank=True, max_length=100, verbose_name='Address')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Description')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
