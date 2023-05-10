# Generated by Django 4.2.1 on 2023-05-09 21:53

import car_collection_app.web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_car_options_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.FloatField(validators=[car_collection_app.web.models.validate_car_price]),
        ),
    ]
