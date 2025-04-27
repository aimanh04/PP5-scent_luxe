from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'created_at', 'read')