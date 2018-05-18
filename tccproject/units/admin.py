from django.contrib import admin
from units.models import Unit

class UnitModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')
    autocomplete_fields = ('course',)
    search_fields = ('title',)
    list_filter = ('course',)
    
admin.site.register(Unit, UnitModelAdmin)
