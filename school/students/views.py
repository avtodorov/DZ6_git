import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

import factory

from faker import Faker

from students.forms import StudentForm
from students.models import Student


# Create your views here.

# path('students/', views.get_students),
def get_students(request):
    queryset = Student.objects.all()
    context = {'students': queryset}

    return render(request, 'students/s_index.html', context)


# path('students/<int:student_id>/', views.get_student),
def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'GET':
        form = StudentForm(instance=student)
        context = {'form': form}

        return render(request, 'students/edit.html', context)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students:list'))

        return render(request, 'students/edit.html', context={'form': form})

    return HttpResponse(status=405)


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

        return render(request, 'students/create.html', context={'form': form})

    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('students:list'))
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
