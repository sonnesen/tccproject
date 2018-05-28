from django.contrib import admin

from documents.models import Document


class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uri', 'course',)
    search_fields = ('name',)
    autocomplete_fields = ('course',)
    list_filter = ('name',)


admin.site.register(Document, DocumentModelAdmin)
