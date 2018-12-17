# Generated by Django 2.1.1 on 2018-09-09 19:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hotelweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 839263, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='alerttype',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 840014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 837003, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 836828, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 836800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chats',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 836385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 831893, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 841627, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dispatchstock',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 848309, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='drink',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 841124, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 835777, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 835736, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 835707, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facilities',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 832747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facilitytype',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 849189, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='food',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 840590, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='guests',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 847784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 845537, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 846418, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='laundrytype',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 847294, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='menu',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 843299, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='menu',
            name='status_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 843233, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 844464, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 843949, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 843869, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packages',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 845974, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='parking',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 835199, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 834704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requests',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 837593, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requesttype',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 838495, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 829757, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 848772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 842152, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplies',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 842678, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 828762, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usertrackingmovements',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 845000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 838045, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 833958, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='workers',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 9, 19, 8, 24, 830962, tzinfo=utc)),
        ),
    ]