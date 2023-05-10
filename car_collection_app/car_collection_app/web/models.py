from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


def validate_age(value):
    if value < 18:
        raise ValidationError('You must be at least 18 years old')


def validation_car_year(value):
    if int(value) < 1980 or int(value) > 2049:
        raise ValidationError("Year must be between 1980 and 2049")


def validate_car_price(value):
    if int(value) < 1:
        raise ValidationError('Price cannot be below 1.00 $')


# PROFILE MODEL.
class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    PASSWORD_MAX_LEN = 30

    PROFILE_MAX_LEN = 10
    MIN_LEN_PROFILE = 2
    MIN_LEN_VALIDATION_ERROR_MSG = "The username must be a minimum of 2 chars"

    username = models.CharField(
        max_length=PROFILE_MAX_LEN,
        validators=(
            MinLengthValidator(MIN_LEN_PROFILE, message=MIN_LEN_VALIDATION_ERROR_MSG),
        ),

        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        validators=(
            validate_age,
        ),
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'id={self.id} username={self.username} email={self.email} age={self.age}'

    class Meta:
        ordering = ('id',)

# CAR MODEL.
class Car(models.Model):
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    CAR_TYPE_MAX_LEN = 10
    CAR_MODEL_MAX_LEN = 20
    CAR_MODEL_MIN_LEN = 2
    CAR_PRICE_MIN_VALUE = 1.0

    type = models.CharField(
        max_length=CAR_TYPE_MAX_LEN,
        choices=CAR_TYPES,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=CAR_MODEL_MAX_LEN,
        blank=False,
        null=False,
    )

    year = models.PositiveIntegerField(
        validators=(
            validation_car_year,
        ),
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=(
            validate_car_price,
        ),
        blank=False,
        null=False,
    )


    def __str__(self):
        return f'id={self.id} type={self.type} model={self.model} year={self.year} price{self.price}$'

    class Meta:
        ordering = ('id',)


