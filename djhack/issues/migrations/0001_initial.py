# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-11 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0001_initial'),
        ('Empinf', '0004_remove_employee_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('issueid', models.IntegerField(default=1, unique=True)),
                ('priority', models.IntegerField(default=2)),
                ('complaint_date', models.DateTimeField(auto_now_add=True)),
                ('summary', models.CharField(default='unassigned', max_length=1024)),
                ('resolve', models.BooleanField(default='False')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empinf.Employee')),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Cust')),
            ],
        ),
    ]
