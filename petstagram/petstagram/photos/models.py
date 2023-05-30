from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size_5mb

UserModel = get_user_model()


class Photo(models.Model):
    PHOTO_DESCRIPTION_MAX_LEN = 300
    PHOTO_DESCRIPTION_MIN_LEN = 10
    PHOTO_LOCATION_MAX_LEN = 30

    photo = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size_5mb,
        ),
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=PHOTO_DESCRIPTION_MAX_LEN,
        validators=(MinLengthValidator(PHOTO_DESCRIPTION_MIN_LEN),),
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=PHOTO_LOCATION_MAX_LEN,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
