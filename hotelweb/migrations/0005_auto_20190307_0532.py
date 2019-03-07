# Generated by Django 2.1.1 on 2019-03-07 05:32

from django.db import migrations, models
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('hotelweb', '0004_auto_20190306_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobshift',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False),
        ),
    ]
