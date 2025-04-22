from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    This adds text editing of the body in admin panel
    """
    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)