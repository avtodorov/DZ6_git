import random

from django.core.management import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='def is 100 rows', nargs='?', default=100)

    def handle(self, count, **options):
        fake = Faker()
        theme = ['Python', 'PHP', 'Java', 'UI/UX', 'QA', 'Recruiting/HR', 'Marketing', 'MachineLearning']
        teachers = [
            Teacher(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                theme=theme[(random.randint(0, 7))]
            )
            for _ in range(count)
        ]

        Teacher.objects.bulk_create(teachers)

        print(f'{count} teachers have been generated and saved to DB')
