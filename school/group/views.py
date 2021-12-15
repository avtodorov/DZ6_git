# from django.shortcuts import render
import random

from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from faker import Faker

from group.forms import GroupForm
from group.models import Group


# Create your views here.
# path('groups/', group_views.get_groups),
def group_index(request):
    groups = Group.objects.all()
    content = {'groups': groups}
    return render(request, 'g_index.html', content)


# path('groups/int:group_id>/', group_views.get_group),
def get_group(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
        response = model_to_dict(group)

    except Group.DoesNotExist:
        response = {
            'error': f'Does not Exist teacher with id ={group_id}'
        }

    return JsonResponse(response)


# path('create/', views.create_group, name='create_group')
@require_http_methods(['GET', 'POST'])
def create_group(request):
    if request.method == "GET":
        fake = Faker()
        theme = ['Python', 'PHP', 'Java', 'UI/UX', 'QA', 'Recruiting/HR', 'Marketing', 'MachineLearning']

        position = random.randint(0, 7)

        data = {
            'group_name': f'{theme[position]} ...',
            'group_theme': theme[position],
            'teacher': fake.first_name()
        }

        form = GroupForm(initial=data)

        return render(request, 'create-group.html', context={'form': form})

    form = GroupForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('group:group_index'))
    return HttpResponse(form.errors['theme'], status=200)
