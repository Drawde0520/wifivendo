# Generated by Django 2.2.7 on 2019-11-27 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_auto_20191127_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinqueue',
            name='Total_Time',
            field=models.DurationField(blank=True, default=datetime.timedelta(0), null=True),
        ),
    ]