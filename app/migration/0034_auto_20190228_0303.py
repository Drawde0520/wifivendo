# Generated by Django 2.1.7 on 2019-02-27 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20190228_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='Last_Update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
