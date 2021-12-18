from django import forms
from django.core.exceptions import ValidationError

from group.models import Group


class GroupForm(forms.ModelForm):
    def clean_group_theme(self):
        themes = ['Python', 'PHP', 'Java', 'UI/UX', 'QA', 'Recruiting/HR', 'Marketing', 'MachineLearning']
        theme = self.cleaned_data['theme']

        if theme not in themes:
            raise ValidationError(f"This theme is not aloud.\n "
                                  f"Choices are: {' '.join(themes)}")

        return theme

    class Meta:
        model = Group
        fields = (
            'group_name',
            'group_theme',
            'teacher',
        )
