# Generated by Django 3.2 on 2021-04-30 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='image',
            field=models.ImageField(default=datetime.datetime(2021, 4, 30, 14, 25, 11, 460350, tzinfo=utc), upload_to='media/'),
        ),
    ]
