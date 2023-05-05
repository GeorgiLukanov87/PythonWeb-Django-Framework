from django.core import validators
from django.db import models

from my_plant_app.web.helper.validators import validate_firstname, validate_plant_name


# Profile Model
class Profile(models.Model):
    MIN_USERNAME_LEN = 2

    username = models.CharField(
        max_length=10,
        validators=(
            validators.MinLengthValidator(MIN_USERNAME_LEN),
        ),

        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=20,
        validators=(
            validate_firstname,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=20,
        validators=(
            validate_firstname,
        ),
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


# Plant Model
class Plant(models.Model):
    MIN_PLANT_NAME_LEN = 2
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'
    PLANTS_TYPES = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    type = models.CharField(
        max_length=14,
        choices=PLANTS_TYPES,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(MIN_PLANT_NAME_LEN),
            validate_plant_name,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
