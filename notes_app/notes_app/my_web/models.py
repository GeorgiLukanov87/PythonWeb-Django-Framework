from django.db import models


class Profile(models.Model):
    PROFILE_FIST_NAME_MAX_LEN = 20
    PROFILE_LAST_NAME_MAX_LEN = 20

    first_name = models.CharField(
        max_length=PROFILE_FIST_NAME_MAX_LEN,
    )

    last_name = models.CharField(
        max_length=PROFILE_LAST_NAME_MAX_LEN,
    )

    age = models.PositiveIntegerField()
    image_url = models.URLField()


class Note(models.Model):
    NOTE_TITLE_MAX_LEN = 30
    title = models.CharField(
        max_length=NOTE_TITLE_MAX_LEN,
    )

    image_url = models.URLField()
    content = models.TextField()
