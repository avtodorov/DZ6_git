from django.shortcuts import render


# Create your views here.

# path('', views.index),
def index(request):
    return render(request, 'mainpage/index.html')
