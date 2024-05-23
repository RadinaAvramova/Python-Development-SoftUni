from django.core.validators import MinLengthValidator
from django.db import models

from myMusicApp.core.validators import validate_chars_username


# Create your models here.
class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 2

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME),
            validate_chars_username,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    