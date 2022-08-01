# Generated by Django 3.0.3 on 2020-03-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0079_device_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whitelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MAC_Address', models.CharField(max_length=255, unique=True, verbose_name='MAC')),
                ('Device_Name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Whitelisted Devices',
                'verbose_name_plural': 'Whitelisted Devices',
            },
        ),
    ]
