# Generated by Django 3.1.7 on 2024-09-26 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_allproduct_brandproductid'),
        ('promotion', '0005_listptomo_brandproductid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listptomo',
            name='brandproductid',
        ),
        migrations.AddField(
            model_name='listptomo',
            name='brandid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brandids', to='product.allproduct'),
        ),
    ]
