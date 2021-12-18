from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.


from .models import Group


class GroupAdmin(ModelAdmin):
    list_display = ('group_name', 'group_theme', 'teacher',)
    list_display_links = ('group_name',)  # links from admin to edit
    fields = ('group_name', 'group_theme', 'teacher',)

    def get_queryset(self, request):
        return Group.objects.all()


admin.site.register(Group, GroupAdmin)
