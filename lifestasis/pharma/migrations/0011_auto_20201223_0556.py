# Generated by Django 3.0.7 on 2020-12-23 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0010_auto_20201223_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='prescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharma.Prescription'),
        ),
    ]
