# Generated by Django 3.2.9 on 2021-12-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='execution_time',
            field=models.FloatField(max_length=10),
        ),
    ]
