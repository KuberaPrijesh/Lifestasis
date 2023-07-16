# Generated by Django 3.0.7 on 2020-12-23 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0012_bill_billunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='contact_num',
            field=models.CharField(default=1234567890, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='name',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
    ]
