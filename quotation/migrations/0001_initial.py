# Generated by Django 3.1.7 on 2024-08-05 08:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('tel_number', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('tax_number', models.CharField(blank=True, max_length=50, null=True)),
                ('email_addess', models.CharField(blank=True, max_length=50, null=True)),
                ('quotation_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('buy_item', models.BooleanField(default=False, help_text='ลูกค้าซื้อหรือเปล่า')),
                ('brance', models.CharField(blank=True, max_length=300, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'tel_number')},
            },
        ),
        migrations.CreateModel(
            name='quotation_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('sell_price', models.DecimalField(blank=True, decimal_places=4, help_text='จำนวนเงินที่ออกบิล', max_digits=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quos', to='product.brand')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quos', to='quotation.quotation')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quos', to='product.allproduct')),
            ],
        ),
    ]
