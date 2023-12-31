# Generated by Django 3.0.7 on 2020-12-22 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20201221_0702'),
        ('pharma', '0008_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Cases')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharma.Stock')),
            ],
        ),
    ]
