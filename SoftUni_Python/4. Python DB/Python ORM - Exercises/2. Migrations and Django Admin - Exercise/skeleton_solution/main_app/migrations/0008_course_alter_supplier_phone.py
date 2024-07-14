# Generated by Django 4.2.4 on 2023-10-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('lecturer', models.CharField(max_length=90)),
                ('description', models.TextField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
