# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('importance_level', models.SmallIntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('reminder_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(null=True)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('deck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hands', to='goals.Deck')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='MiniCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minicards', to='goals.Card')),
            ],
        ),
    ]
