from django.urls import path

from students import views

app_name = 'students'

urlpatterns = [
    path('', views.get_students, name='students_list'),
    path('<int:student_id>/', views.get_student, name='student_details'),
    path('create/', views.create_students, name='create_student'),
    # path('generate_students/', views.generate_students),
]
