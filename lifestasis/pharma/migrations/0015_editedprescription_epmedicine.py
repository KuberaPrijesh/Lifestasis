# Generated by Django 3.0.7 on 2020-12-25 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
        ('pharma', '0014_stock_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditedPrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pres', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pharma.Prescription')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admins.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='EPMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharma.Stock')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharma.EditedPrescription')),
            ],
        ),
    ]
