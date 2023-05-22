from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    COMMENT_TEXT_MAX_LEN = 300
    text = models.TextField(
        max_length=COMMENT_TEXT_MAX_LEN,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )

