from django.core.exceptions import ValidationError


def validate_first_letter(name):
    if not name[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def validate_all_letters(name):
    if not name.isalpha():
        raise ValidationError('Fruit name should contain only letters!')