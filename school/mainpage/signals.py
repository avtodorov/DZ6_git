from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from mainpage.models import Contact

from .tasks import send_email


@receiver(post_save, sender=Contact)
def email_signl(sender, instance, **kwargs):
    context = {
        'email': instance.email,
        'subject': instance.subject,
        'message': instance.message,
    }
    send_email.delay(**context)
