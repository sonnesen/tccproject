from django.contrib import admin

from videos.models import Video


class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uri', 'unit',)
    search_fields = ('name',)
    autocomplete_fields = ('unit',)
    list_filter = ('name',)


admin.site.register(Video, VideoModelAdmin)
