# Generated by Django 2.1.1 on 2019-03-07 07:09

from django.db import migrations, models
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('hotelweb', '0006_auto_20190307_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='facility_capacity',
            field=models.IntegerField(default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='facilitytype',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False),
        ),
    ]
