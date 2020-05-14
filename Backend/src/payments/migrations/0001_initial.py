# Generated by Django 3.0.3 on 2020-05-14 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bancks', '0001_initial'),
        ('users', '0001_initial'),
        ('factures', '0003_auto_20200514_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('codePayment', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuePayment', models.PositiveIntegerField()),
                ('datePayment', models.DateTimeField(auto_now_add=True)),
                ('facturaPayment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='factures.InvoiceServices')),
            ],
        ),
        migrations.CreateModel(
            name='DirectPayment',
            fields=[
                ('codeDirectPayment', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payments.Payment')),
                ('workerPayment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='users.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='BanckPayment',
            fields=[
                ('codeBanckPayment', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banckPayment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='bancks.Banck')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payments.Payment')),
            ],
        ),
    ]