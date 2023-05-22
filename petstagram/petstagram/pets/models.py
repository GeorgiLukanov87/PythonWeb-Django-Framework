from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    PET_NAME_MAX_LEN = 30

    name = models.CharField(
        max_length=PET_NAME_MAX_LEN,
        blank=False,
        null=False,
    )

    personal_photo = models.URLField(
        blank=False,
        null=False,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
