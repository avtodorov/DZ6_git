from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import Contact


# Register your models here.

class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message',)
    list_display_links = ('name',)  # links from admin to edit
    fields = ('name', 'email', 'subject', 'message',)


admin.site.register(Contact, ContactAdmin)
