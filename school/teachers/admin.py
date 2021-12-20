from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.


from .models import Teacher


class TeacherAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'theme',)
    list_display_links = ('first_name',)  # links from admin to edit
    fields = ('first_name', 'last_name', 'theme',)

    def get_queryset(self, request):
        return Teacher.objects.all()


admin.site.register(Teacher, TeacherAdmin)
