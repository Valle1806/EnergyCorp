# Generated by Django 3.0.3 on 2020-05-21 21:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0005_delete_commercialinvoice'),
        ('contract', '0025_auto_20200521_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='publicity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='commercial.Commercial'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='deadDatePay',
            field=models.DateField(default=datetime.datetime(2020, 5, 31, 21, 8, 9, 772882)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='interestMora',
            field=models.FloatField(default=0.0),
        ),
    ]