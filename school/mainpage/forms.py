from django import forms
from django.core.exceptions import ValidationError

from mainpage.models import Contact


class ContactForm(forms.ModelForm):

    # def is_valid(self):
    #     pass

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )
