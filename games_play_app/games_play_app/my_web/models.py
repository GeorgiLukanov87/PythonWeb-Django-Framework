from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def validate_rating(value):
    if float(value) < 0.1 or float(value) > 5.0:
        raise ValidationError('The rating can be between 0.1 and 5.0 (both inclusive)')


class Profile(models.Model):
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    AGE_MIN_VALUE = 12

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE, message=None),
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
        return f'id={self.id}, email={self.email}'

    class Meta:
        ordering = ('id',)


class Game(models.Model):
    GAME_TITLE_MAX_LEN = 30
    GAME_CATEGORY_MAX_LEN = 15
    GAME_MAX_LEVEL_LIMIT = 1

    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = 'Other'

    GAME_CATEGORIES = (
        (ACTION, ACTION),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    )

    title = models.CharField(
        max_length=GAME_TITLE_MAX_LEN,
        unique=True,
        blank=False,
        null=False,
    )

    category = models.CharField(
        max_length=GAME_CATEGORY_MAX_LEN,
        choices=GAME_CATEGORIES,
        blank=False,
        null=False,
    )

    rating = models.FloatField(
        validators=(
            validate_rating,
        ),
        blank=False,
        null=False,
    )

    max_level = models.PositiveIntegerField(
        validators=(
            MinValueValidator(GAME_MAX_LEVEL_LIMIT, message=None),
        ),

        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    summary = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'id={self.id}, {self.title}'

    class Meta:
        ordering = ('id',)
