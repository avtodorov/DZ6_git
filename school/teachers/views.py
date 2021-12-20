import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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

    return render(request, 'teachers/t_index.html', context)


# path('teachers/<int:teacher_id>/', teachers_views.get_teacher),
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'GET':
        form = TeacherForm(instance=teacher)
        context = {'form': form}

        return render(request, 'teachers/edit.html', context)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        context = {'form': form}

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

        return render(request, 'teachers/edit.html', context)

    return HttpResponse(status=405)


#
@require_http_methods(['GET', 'POST'])
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/edit.html')


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

        return render(request, 'teachers/create-teacher.html', context={'form': form})

    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teachers:list'))
    return HttpResponse(form.errors['theme'], status=200)
