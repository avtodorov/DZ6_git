from django import forms
from django.core.exceptions import ValidationError

from teachers.models import Teacher


class TeacherForm(forms.ModelForm):
    def clean_theme(self):
        themes = ['Python', 'PHP', 'Java', 'UI/UX', 'QA', 'Recruiting/HR', 'Marketing', 'MachineLearning']
        theme = self.cleaned_data['theme']

        if theme not in themes:
            raise ValidationError(f"This theme is not aloud.\n "
                                  f"Choices are: {' '.join(themes)}")

        return theme

    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'theme'
        )
