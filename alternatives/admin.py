from django.contrib import admin

from alternatives.models import Alternative


class AlternativeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'question', 'is_correct',)
    search_fields = ('description', )
    autocomplete_fields = ('question',)
    list_filter = ('question', 'is_correct')


admin.site.register(Alternative, AlternativeModelAdmin)