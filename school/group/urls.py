from django.urls import path

from group import views

app_name = 'group'

urlpatterns = [
    path('', views.group_index, name='group_index'),
    path('<int:group_id>/', views.get_group, name='group_details'),
    path('create/', views.create_group, name='create_group')
]
