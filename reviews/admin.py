from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'title', 'rating', 'created_on')
    list_filter = ('rating', 'created_on')
    search_fields = ('user__username', 'product__name', 'title', 'body')
    ordering = ('-created_on',)
