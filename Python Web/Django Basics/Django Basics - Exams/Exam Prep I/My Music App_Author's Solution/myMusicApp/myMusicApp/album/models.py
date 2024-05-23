from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Album(models.Model):

    MAX_LEN = 30
    GENRES = ["Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", "Other"]
    CHOICES = tuple([(c, c) for c in GENRES])

    album_name = models.CharField(
        max_length=MAX_LEN,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name'
    )
    artist = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,

        choices=CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        ),
        null=False,
        blank=False,

    )

    owner = models.ForeignKey(
        'user_profile.Profile',
        on_delete=models.CASCADE,
        related_name='albums',
    )

