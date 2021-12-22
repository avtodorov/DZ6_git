from django import forms
from django.core.exceptions import ValidationError

from students.models import Student


class StudentForm(forms.ModelForm):

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 17:
            raise ValidationError('The person is too young yet.')

        return age  # need this, cause method should return value. othervs it'll return None.

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
            'rating',
        )
