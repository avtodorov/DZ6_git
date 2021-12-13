import random

from django.forms.models import model_to_dict
from django.http import Http404, HttpResponse, JsonResponse

import factory

from faker import Faker

from students.models import Student


# Create your views here.
# path('', views.index),
def index(request):
    return HttpResponse('<h1> Welcome to our school !</h1>')


# path('students/', views.get_students),
def get_students(request):
    students = [
        {
            'first_name': student.first_name,
            'last_name': student.last_name,
            'age': student.age

        }
        for student in Student.objects.all()  # возвращает QuerySet
    ]

    data = {
        # то же самое что: SELECT count(*) FROM students_student
        'count': Student.objects.count(),
        'students': students,
    }

    return JsonResponse(data)  # JsonResponse возвращает только dict


# path('students/<int:student_id>/', views.get_student),
def get_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
        response = model_to_dict(student)

    except Student.DoesNotExist:
        # response = {
        #     'error': f'Does not Exist student with id ={student_id}'
        # }
        raise Http404

    return JsonResponse(response)


# path('students/create/<int:age>/', views.create_students)
def create_students(request, age):
    fake = Faker()

    data = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'age': age,
    }

    student = Student(**data)
    student.save()

    return JsonResponse(data)


# path('students/generate_students/', views.generate_students)
def generate_students(request):
    # fake = Faker()

    qtt_students = {
        'count': request.GET.get('count')
    }
    # validation "!< 0, <100, != float"
    try:
        qtt = int(qtt_students['count'])
        if 100 < qtt or qtt < 0:
            raise ValueError
    except KeyError:
        pass

    StudentFactory.create_batch(int(qtt_students['count']))

    return HttpResponse(f'{qtt_students["count"]} student(s)'
                        f'list was successfully generated')


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(19, 39)
