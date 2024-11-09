# Generated by Django 3.1.7 on 2024-07-19 07:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
import invoice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('name_invoce', models.CharField(blank=True, max_length=300, null=True)),
                ('tel_number', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('address_invoice', models.TextField(blank=True, null=True)),
                ('tax_number', models.CharField(blank=True, max_length=50, null=True)),
                ('email_addess', models.CharField(blank=True, max_length=50, null=True)),
                ('invoice_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('billable', models.BooleanField(default=False)),
                ('ler_pickup', models.BooleanField(default=False)),
                ('ler_receive', models.CharField(blank=True, max_length=100, null=True)),
                ('ler_deliver', models.CharField(blank=True, max_length=100, null=True)),
                ('ler_print', models.BooleanField(default=False)),
                ('ler_note', models.TextField(blank=True, null=True)),
                ('ler_expected_d', models.CharField(blank=True, max_length=100, null=True)),
                ('ler_priority', models.IntegerField(blank=True, null=True)),
                ('ler_map', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_etax', models.BooleanField(default=False, help_text='ลูกค้าต้องการออก e-tax')),
                ('invoice', models.BooleanField(default=True, help_text='ถ้าเก็บ stock ไม่ต้องใส่')),
                ('paid', models.BooleanField(default=False)),
                ('invoice_eve', models.CharField(blank=True, max_length=50, null=True)),
                ('count_invoice_number', models.CharField(blank=True, max_length=9, null=True)),
                ('invoice_tst', models.CharField(blank=True, max_length=9, null=True)),
                ('print_tst', models.BooleanField(default=False)),
                ('delivery_date', models.CharField(blank=True, max_length=100, null=True)),
                ('evenote', models.TextField(blank=True, null=True)),
                ('map_pic', models.ImageField(blank=True, max_length=500, null=True, upload_to=invoice.models.map_img)),
                ('receive_pic', models.ImageField(blank=True, max_length=500, null=True, upload_to=invoice.models.receive_img)),
                ('brance', models.CharField(blank=True, max_length=300, null=True)),
                ('etax', models.BooleanField(default=False)),
                ('urgent_need_invoice', models.BooleanField(default=False)),
                ('send_etax_email', models.BooleanField(default=True)),
                ('cancel_inv', models.BooleanField(default=False)),
                ('cancel_date', models.DateField(blank=True, help_text='วันที่ยกเลิก', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'tel_number')},
            },
        ),
        migrations.CreateModel(
            name='invoice_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(blank=True, choices=[('Shopee', 'Shopee'), ('Lazada', 'Lazada'), ('Nocnoc', 'Nocnoc'), ('Website&Line&FB', 'Website&Line&FB'), ('Others', 'Others')], default='', max_length=20, null=True)),
                ('qty', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('received', models.DecimalField(blank=True, decimal_places=3, help_text='จำนวนเงินที่ได้รับ', max_digits=10, null=True)),
                ('sell_price', models.DecimalField(blank=True, decimal_places=4, help_text='จำนวนเงินที่ออกบิล', max_digits=10, null=True)),
                ('real_price', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('gp', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('paymentmade', models.BooleanField(default=False)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('money_collect', models.BooleanField(default=False)),
                ('collect_date', models.DateField(blank=True, null=True)),
                ('coment_invoice', models.CharField(blank=True, max_length=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='product.brand')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='invoice.invoice')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='product.allproduct')),
            ],
        ),
    ]
