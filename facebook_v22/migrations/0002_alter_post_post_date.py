# Generated by Django 4.2.4 on 2023-08-14 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_v22', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 14, 14, 32, 52, 955187)),
        ),
    ]
