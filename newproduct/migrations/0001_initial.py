# Generated by Django 3.1.7 on 2024-09-16 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=300, null=True)),
                ('product_name', models.CharField(blank=True, max_length=300, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('link_product', models.CharField(blank=True, max_length=300, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=500, null=True)),
                ('status_create', models.BooleanField(default=False)),
                ('status_shopee', models.BooleanField(default=False)),
                ('status_lazada', models.BooleanField(default=False)),
                ('status_nocnoc', models.BooleanField(default=False)),
                ('status_tiktok', models.BooleanField(default=False)),
                ('status_mainweb', models.BooleanField(default=False)),
                ('vdo', models.BooleanField(default=False)),
                ('low_quality', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=300, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
