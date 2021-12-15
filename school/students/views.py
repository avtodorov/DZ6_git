import random

from django.forms.models import model_to_dict
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

import factory

from faker import Faker

from students.forms import StudentForm
from students.models import Student

# Create your views here.
# path('', views.index),
# def index(request):
#     return HttpResponse('<h1> Welcome to our school !</h1>')


# path('students/', views.get_students),
def get_students(request):
    queryset = Student.objects.all()
    context = {'students': queryset}

    return render(request, 's_index.html', context)


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
@require_http_methods(['GET', 'POST'])
def create_students(request):
    if request.method == "GET":
        fake = Faker()

        data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': random.randint(17, 60),
        }

        form = StudentForm(initial=data)

        return render(request, 'create-student.html', context={'form': form})

    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('students:students_list'))
    return HttpResponse(str(form.errors), status=400)


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
