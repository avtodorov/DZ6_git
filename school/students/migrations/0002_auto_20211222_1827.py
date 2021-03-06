# Generated by Django 3.2.9 on 2021-12-22 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(default='B', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='rating',
            field=models.PositiveSmallIntegerField(default=85, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
    ]
