from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.core import custom_validators
from fruitipedia.user_profile.models import Profile


class Fruit(models.Model):
    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    fruit_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(MinLengthValidator(MIN_LEN_NAME), custom_validators.validate_all_letters,),
        null=False,
        blank=False,
        unique=True,
        verbose_name='Name'
    )
    fruit_image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition_info = models.TextField(
        null=True,
        blank=True,
        verbose_name='Nutrition',
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )


