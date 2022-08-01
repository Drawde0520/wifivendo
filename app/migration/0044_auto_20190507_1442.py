# Generated by Django 2.1.7 on 2019-05-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_device'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'Device', 'verbose_name_plural': 'Device'},
        ),
        migrations.AddField(
            model_name='rates',
            name='Pulse',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]