from django.contrib import admin

from courses.models import Course
from units.models import Unit


class UnitInlineModelAdmin(admin.TabularInline):
    model = Unit
    min_num = 1
    extra = 0
    
    
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category', 'instructor', 'keyword_list')
    autocomplete_fields = ('category', 'instructor')
    readonly_fields = ('created_at',)
    list_filter = ('title', 'category', 'instructor')
    search_fields = ('title', 'category', 'instructor')
    inlines = [UnitInlineModelAdmin]
    
    def get_queryset(self, request):
        return super(
            CourseModelAdmin, self).get_queryset(request).prefetch_related('keywords')

    def keyword_list(self, obj):
        return ", ".join(o.name for o in obj.keywords.all())

    
admin.site.register(Course, CourseModelAdmin)
