# Generated by Django 4.2.6 on 2023-10-08 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='booking_value',
            field=models.FloatField(),
        ),
    ]
