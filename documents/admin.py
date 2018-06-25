from django.contrib import admin

from documents.models import Document

@admin.register(Document)
class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'uri', 'course',)
    search_fields = ('name',)
    autocomplete_fields = ('course',)
    list_filter = ('name',)
