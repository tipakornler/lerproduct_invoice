# Generated by Django 3.1.7 on 2024-06-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_auto_20240612_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='trans',
            name='other_receive',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='รายได้ค่าขนส่งอื่นๆ', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='trans',
            name='receive',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='รายได้ค่าขนส่ง', max_digits=10, null=True),
        ),
    ]
