from django.db import models


class Profile(models.Model):
    PROFILE_FIRST_NAME_MAX_LEN = 30
    PROFILE_LAST_NAME_MAX_LEN = 30

    first_name = models.CharField(
        max_length=PROFILE_FIRST_NAME_MAX_LEN,
    )
    last_name = models.CharField(
        max_length=PROFILE_LAST_NAME_MAX_LEN,
    )
    image_url = models.URLField()

    def __str__(self):
        return f'Name={self.first_name}, Last name={self.last_name}, id={self.id}'


class Book(models.Model):
    BOOK_TITLE_MAX_LEN = 30
    BOOK_TYPE_MAX_LEN = 30

    title = models.CharField(
        max_length=BOOK_TITLE_MAX_LEN,
    )
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(
        max_length=BOOK_TYPE_MAX_LEN,
    )

    def __str__(self):
        return f'Book title={self.title}, id={self.id}, type={self.type}'
