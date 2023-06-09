# Generated by Django 4.2.1 on 2023-05-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
