# Generated by Django 3.2 on 2021-05-03 03:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_recipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(default=datetime.datetime(2021, 5, 3, 3, 44, 38, 459914, tzinfo=utc), upload_to='pictures/'),
        ),
    ]
