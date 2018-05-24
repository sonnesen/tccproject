from django.contrib import admin

from activities.models import Activity
from units.models import Unit


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 1
    verbose_name = 'Unit Activity'
    verbose_name_plural = 'Unit Activities'
    

class UnitModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')
    autocomplete_fields = ('course',)
    search_fields = ('title',)
    list_filter = ('course',)
    inlines = [ActivityInline, ]

    
admin.site.register(Unit, UnitModelAdmin)
