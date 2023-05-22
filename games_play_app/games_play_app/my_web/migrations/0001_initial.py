# Generated by Django 4.2.1 on 2023-05-16 11:39

import django.core.validators
from django.db import migrations, models
import games_play_app.my_web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('Action', 'Action'), ('Puzzle', 'Puzzle'), ('Strategy', 'Strategy'), ('Sports', 'Sports'), ('Board/Card Game', 'Board/Card Game'), ('Other', 'Other')], max_length=15)),
                ('rating', models.FloatField(validators=[games_play_app.my_web.models.validate_rating])),
                ('max_level', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1, message=None)])),
                ('image_url', models.URLField()),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(12, message=None)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]