# Generated by Django 3.2.3 on 2023-07-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
