from django.urls import path

from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('', views.get_teachers, name='teachers_list'),
    path('<int:teacher_id>/', views.get_teacher, name='teacher_details'),
    path('create/', views.create_teacher, name='create_teacher'),
    # path('generate_students/', views.generate_students),
]
