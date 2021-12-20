from django.urls import path

from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('', views.get_teachers, name='list'),
    path('create/', views.create_teacher, name='create'),
    path('<int:teacher_id>/edit', views.edit_teacher, name='edit'),
    path('<int:teacher_id>/delete', views.delete_teacher, name='delete_teacher'),
    # path('<int:teacher_id>/', views.get_teacher, name='details'),
    # path('generate_students/', views.generate_students),
]
