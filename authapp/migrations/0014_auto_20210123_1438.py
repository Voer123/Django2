# Generated by Django 2.0 on 2021-01-23 05:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_auto_20210123_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 5, 38, 44, 637733, tzinfo=utc)),
        ),
    ]
