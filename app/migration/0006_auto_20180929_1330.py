# Generated by Django 2.0.7 on 2018-09-29 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180929_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotstatus',
            name='Client',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]