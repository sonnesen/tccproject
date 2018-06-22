from django.contrib import admin

from courses.models import Course
from units.models import Unit


class UnitInline(admin.TabularInline):
    model = Unit
    extra = 1
    verbose_name = 'Course Unit'
    verbose_name_plural = 'Course Units'

    
@admin.register(Course)    
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'category', 'instructor', 
                    'keyword_list', 'description', 'image')
    autocomplete_fields = ('category', 'instructor')
    readonly_fields = ('created_at',)
    list_filter = ('name', 'category', 'instructor')
    search_fields = ('name', 'category', 'instructor')
    inlines = [UnitInline, ]
    
    def get_queryset(self, request):
        return super(
            CourseModelAdmin, self).get_queryset(
                request).prefetch_related('keywords')

    def keyword_list(self, obj):
        return ", ".join(o.name for o in obj.keywords.all())

