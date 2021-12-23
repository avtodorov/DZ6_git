from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from mainpage.phone_validator import validate_phone


# Create your models here.
class Student(models.Model):
    # id = models.BigAutoField
    first_name = models.CharField(max_length=64)  # тип данных Char (строчный), длина 64 символа
    last_name = models.CharField(max_length=64)  # по умолчанию все колонки обязательные, поэтому :
    age = models.PositiveSmallIntegerField()  # параметр null = True, если колонка в БД не обязательная
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )
    grade = models.CharField(max_length=1)
    phone = models.CharField(
        max_length=13,
        validators=[validate_phone]
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_info(self):
        return f'{self.id} {self.first_name} {self.last_name}, age = {self.age}'

    def __str__(self):
        return self.get_full_info()
