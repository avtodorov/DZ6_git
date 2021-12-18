from django.urls import path

from students import views

app_name = 'students'

urlpatterns = [
    path('', views.get_students, name='list'),
    path('create/', views.create_students, name='create'),
    path('<int:student_id>/edit/', views.edit_student, name='edit'),
    # path('<int:student_id>/', views.get_student, name='student_details'),
    # path('generate_students/', views.generate_students),
]
