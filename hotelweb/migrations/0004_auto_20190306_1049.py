# Generated by Django 2.1.1 on 2019-03-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelweb', '0003_auto_20190306_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_hr',
        ),
        migrations.AddField(
            model_name='staff',
            name='is_hr',
            field=models.BooleanField(default=False),
        ),
    ]
