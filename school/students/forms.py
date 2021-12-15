from django import forms
from django.core.exceptions import ValidationError

from students.models import Student


class StudentForm(forms.ModelForm):

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 17:
            raise ValidationError('The person is too young yet.')

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'age',
        )
