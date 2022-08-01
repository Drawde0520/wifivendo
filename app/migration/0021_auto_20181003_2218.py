# Generated by Django 2.0.7 on 2018-10-03 14:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20181001_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinslot',
            name='Slot_ID',
            field=models.CharField(default='n8cy3oKCKM', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clients',
            name='Last_Update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 14, 16, 35, 985265, tzinfo=utc)),
        ),
    ]
