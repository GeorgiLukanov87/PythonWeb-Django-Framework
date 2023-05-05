# Raise error if value(Profile username) starts with lower letter.
from django.core.exceptions import ValidationError


def validate_firstname(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


# Raise if value(plant name) contains digit.
def validate_plant_name(value):
    for char in value:
        if char.isspace():
            continue
        if not char.isalpha():
            raise ValidationError("Plant name should contain only letters!")
