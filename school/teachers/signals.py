from django.db.models.signals import pre_save
from django.dispatch import receiver

from teachers.models import Teacher


@receiver(pre_save, sender=Teacher)
def capitalize_fn_ln(instance, **kwargs):
    first_name = instance.first_name
    last_name = instance.last_name
    instance.first_name = str.capitalize(first_name)
    instance.last_name = str.capitalize(last_name)
