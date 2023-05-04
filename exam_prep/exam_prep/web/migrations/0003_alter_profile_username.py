# Generated by Django 4.1.6 on 2023-02-13 12:45

import django.core.validators
from django.db import migrations, models
import exam_prep.web.models


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(
                max_length=15,
                validators=[django.core.validators.MinLengthValidator(2),
                            exam_prep.web.models.validate_username]),
        ),
    ]
