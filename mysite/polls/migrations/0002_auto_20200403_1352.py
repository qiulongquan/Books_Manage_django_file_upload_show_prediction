# Generated by Django 3.0.3 on 2020-04-03 04:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 4, 52, 8, 984470, tzinfo=utc)),
        ),
    ]