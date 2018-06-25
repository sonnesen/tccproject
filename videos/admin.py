from django.contrib import admin

from videos.models import Video


@admin.register(Video)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'uri', 'unit',)
    search_fields = ('name',)
    autocomplete_fields = ('unit',)
    list_filter = ('name',)
    
    def has_add_permission(self, request):
        return False
