# Generated by Django 3.1.7 on 2024-09-24 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_allproduct_brandproductid'),
    ]

    operations = [
        migrations.CreateModel(
            name='listptomo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normal_price', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('promotion_price', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='promotions', to='product.allproduct')),
            ],
        ),
    ]