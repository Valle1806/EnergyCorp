# Generated by Django 3.0.3 on 2020-05-20 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0018_auto_20200520_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='deadDatePay',
            field=models.DateField(default=datetime.datetime(2020, 5, 30, 20, 3, 24, 416500)),
        ),
    ]
