# Generated by Django 3.2.8 on 2021-12-22 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20211222_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 22, 21, 23, 36, 623068)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.TextField(),
        ),
    ]
