from django.urls import path

from group import views

app_name = 'group'

urlpatterns = [
    path('', views.group_index, name='list'),
    path('<int:group_id>/', views.get_group, name='details'),
    path('create/', views.create_group, name='create')
]
