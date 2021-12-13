from django.core.management import BaseCommand
from django.db.models import Q

from teachers.models import Teacher


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-f', '--first_name', nargs='?', type=str, help='Lookup field first_name')
        parser.add_argument('-l', '--last_name', nargs='?', type=str, help='Lookup field last_name')
        parser.add_argument('-t', '--theme', nargs='?', type=str, help='Lookup field theme')

    def handle(self, *args, **options):

        first_name = options['first_name']
        last_name = options['last_name']
        theme = options['theme']

        if first_name and last_name and theme:
            data = Teacher.objects.filter(Q(theme=theme) & Q(first_name__contains=first_name) & Q(last_name__contains=last_name))
        elif theme and first_name:
            data = Teacher.objects.filter(Q(theme=theme) & Q(first_name__contains=first_name))
        elif theme and last_name:
            data = Teacher.objects.filter(Q(theme=theme) & Q(last_name__contains=last_name))
        elif first_name and last_name:
            data = Teacher.objects.filter(Q(first_name__contains=first_name) & Q(last_name__contains=last_name))
        elif theme:
            data = Teacher.objects.filter(Q(theme=theme))
        elif first_name:
            data = Teacher.objects.filter(Q(first_name__contains=first_name))
        elif last_name:
            data = Teacher.objects.filter(Q(last_name__contains=last_name))
        else:
            data = Teacher.objects.all()

        print(f'Found teachers :{data}')
