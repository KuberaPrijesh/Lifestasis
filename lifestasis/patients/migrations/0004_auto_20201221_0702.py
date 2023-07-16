# Generated by Django 3.0.7 on 2020-12-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_cases_appointed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=5),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female'), ('T', 'trans')], max_length=20),
        ),
    ]