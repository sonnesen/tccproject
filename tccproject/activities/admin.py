from django.contrib import admin

from activities.models import Activity


class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'unit')
    search_fields = ('title',)
    autocomplete_fields = ('unit',)
    list_filter = ('unit',)


admin.site.register(Activity, ActivityModelAdmin)
