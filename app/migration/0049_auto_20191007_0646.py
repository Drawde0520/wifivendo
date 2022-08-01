# Generated by Django 2.1.7 on 2019-10-06 22:46

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20191006_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchers',
            name='Voucher_client',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Client'),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='Voucher_code',
            field=models.CharField(default=app.models.Vouchers.generate_code, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='Voucher_create_date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date/Time'),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='Voucher_status',
            field=models.CharField(choices=[('Used', 'Used'), ('Not Used', 'Not Used'), ('Expired', 'Expired')], max_length=25, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='Voucher_time_value',
            field=models.DurationField(blank=True, help_text='Time value in minutes.', null=True, verbose_name='Time Value'),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='Voucher_used_date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Used Date/Time'),
        ),
    ]