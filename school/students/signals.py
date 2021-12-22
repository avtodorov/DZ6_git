from bisect import bisect

from django.db.models.signals import pre_save
from django.dispatch import receiver

from students.models import Student


@receiver(pre_save, sender=Student)
def evaluate_grading(instance, **kwargs):
    breakpoints = [60, 70, 80, 90]
    grades = 'FDCBA'
    grade_index = bisect(breakpoints, instance.rating)
    instance.grade = grades[grade_index]
