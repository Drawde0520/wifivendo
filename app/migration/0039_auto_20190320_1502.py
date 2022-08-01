# Generated by Django 2.1.7 on 2019-03-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20190320_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinqueue',
            name='Total_Time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='Rate_Type',
            field=models.CharField(choices=[('auto', 'Minutes/Peso'), ('manual', 'Custom Rate')], default='auto', help_text='Select "Minutes/Peso" to use  Minutes / Peso value, else use "Custom Rate" to manually setup Rates based on coin value.', max_length=25),
        ),
    ]