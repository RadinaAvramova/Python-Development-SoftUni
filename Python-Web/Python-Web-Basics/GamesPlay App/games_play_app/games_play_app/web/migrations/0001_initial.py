# Generated by Django 4.2.2 on 2023-06-22 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Title')),
                ('category', models.CharField(choices=[('Strategy', 'Strategy'), ('Adventure', 'Adventure'), ('Action', 'Action'), ('Sports', 'Sports'), ('Other', 'Other'), ('Board/Card Game', 'Board/Card Game'), ('Puzzle', 'Puzzle')], max_length=15, verbose_name='Category')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(1)], verbose_name='Rating')),
                ('max_level', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Max Level')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='Summary')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name')),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Profile Picture')),
            ],
        ),
    ]
