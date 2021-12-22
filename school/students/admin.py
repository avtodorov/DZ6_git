from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.


from .models import Student


class StudentAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'rating', 'grade',)
    list_display_links = ('first_name', )  # links from admin to edit
    fields = ('first_name', 'last_name', 'age', 'rating', 'grade', 'phone')
    readonly_fields = ('age', 'grade')

    def get_queryset(self, request):
        return Student.objects.all()


admin.site.register(Student, StudentAdmin)
