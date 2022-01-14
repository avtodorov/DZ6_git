from django.db import models


# Create your models here.
class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.URLField(max_length=2048)
    execution_time = models.FloatField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.email
