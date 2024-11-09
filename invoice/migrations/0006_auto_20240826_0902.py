# Generated by Django 3.1.7 on 2024-08-26 02:02

from django.db import migrations
import django_resized.forms
import invoice.models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20240825_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={},
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ler_pic1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=500, null=True, quality=50, scale=0.4, size=[1920, 1080], upload_to=invoice.models.pic1_img),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ler_pic2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=500, null=True, quality=50, scale=0.4, size=[1920, 1080], upload_to=invoice.models.pic2_img),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ler_pic3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=500, null=True, quality=50, scale=0.4, size=[1920, 1080], upload_to=invoice.models.pic3_img),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ler_pic4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=500, null=True, quality=50, scale=0.4, size=[1920, 1080], upload_to=invoice.models.pic4_img),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ler_pic5',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=500, null=True, quality=50, scale=0.4, size=[1920, 1080], upload_to=invoice.models.pic5_img),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='ler_pic6',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=500, null=True, quality=50, scale=0.4, size=[1920, 1080], upload_to=invoice.models.pic6_img),
        ),
        migrations.AlterIndexTogether(
            name='invoice',
            index_together=set(),
        ),
    ]