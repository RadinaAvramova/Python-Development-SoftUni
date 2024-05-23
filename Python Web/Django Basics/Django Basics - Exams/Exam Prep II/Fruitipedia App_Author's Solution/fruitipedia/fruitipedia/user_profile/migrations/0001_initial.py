# Generated by Django 5.0 on 2023-12-11 11:09

import django.core.validators
import fruitipedia.core.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), fruitipedia.core.custom_validators.validate_first_letter], verbose_name='First Name')),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), fruitipedia.core.custom_validators.validate_first_letter], verbose_name='Last Name')),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Image URL')),
                ('age', models.PositiveIntegerField(blank=True, default=18)),
            ],
        ),
    ]
