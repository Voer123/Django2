# Generated by Django 2.0 on 2021-01-23 07:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0020_auto_20210123_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 25, 7, 53, 18, 70249, tzinfo=utc)),
        ),
    ]
