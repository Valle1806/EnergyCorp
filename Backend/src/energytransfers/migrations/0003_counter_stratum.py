# Generated by Django 3.0.3 on 2020-05-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energytransfers', '0002_auto_20200514_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='stratum',
            field=models.PositiveSmallIntegerField(default=3),
            preserve_default=False,
        ),
    ]