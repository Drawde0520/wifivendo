# Generated by Django 2.0.7 on 2018-10-08 16:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20181007_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinslot',
            name='Last_Updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 16, 30, 58, 759287, tzinfo=utc)),
            preserve_default=False,
        ),
    ]