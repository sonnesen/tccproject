from django.contrib import admin

from resources.models import Resource


class ResourceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'uri', 'activity')
    search_fields = ('uri',)
    autocomplete_fields = ('activity',)
    list_filter = ('activity',)


admin.site.register(Resource, ResourceModelAdmin)
