# Generated by Django 3.1.2 on 2020-10-11 12:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 11, 12, 44, 10, 343159, tzinfo=utc)),
        ),
    ]