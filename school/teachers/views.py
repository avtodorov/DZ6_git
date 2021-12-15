import random

from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from faker import Faker

from teachers.forms import TeacherForm
from teachers.models import Teacher


# Create your views here.

# path('teachers/', teachers_views.get_teachers),
def get_teachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}

    return render(request, 't_index.html', context)


# path('teachers/<int:teacher_id>/', teachers_views.get_teacher),
def get_teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        response = model_to_dict(teacher)

    except Teacher.DoesNotExist:
        response = {
            'error': f'Does not Exist teacher with id ={teacher_id}'
        }

    return JsonResponse(response)


@require_http_methods(['GET', 'POST'])
def create_teacher(request):
    if request.method == "GET":
        fake = Faker()
        theme = ['Python', 'PHP', 'Java', 'UI/UX', 'QA', 'Recruiting/HR', 'Marketing', 'MachineLearning']

        data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'theme': theme[(random.randint(0, 7))],
        }

        form = TeacherForm(initial=data)

        return render(request, 'create-teacher.html', context={'form': form})

    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teacher:teachers_list'))
    return HttpResponse(form.errors['theme'], status=200)
