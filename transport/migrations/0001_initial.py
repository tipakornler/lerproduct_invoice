# Generated by Django 3.1.14 on 2024-06-08 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateField(blank=True, default=datetime.date.today, null=True, unique=True)),
                ('mile_start', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('mile_stop', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('toll_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fuel_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('other_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('other_cost_remark', models.CharField(blank=True, max_length=300, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]