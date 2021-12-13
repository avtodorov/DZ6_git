# from django.shortcuts import render
from django.http import JsonResponse

from teachers.models import Teacher


# Create your views here.

# path('teachers/', teachers_views.get_teachers),
def get_teachers(request):
    teachers = [
        {
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'theme': teacher.theme

        }
        for teacher in Teacher.objects.all()
    ]

    data = {
        'count': Teacher.objects.count(),
        'teachers': teachers,
    }

    return JsonResponse(data)
