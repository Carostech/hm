# Generated by Django 2.0.7 on 2018-07-05 15:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotelweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 5, 15, 48, 48, 71485, tzinfo=utc)),
        ),
    ]
