from django.contrib import admin

from alternatives.models import Alternative

@admin.register(Alternative)
class AlternativeModelAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_correct', 'course', 'unit', 'exam', 'question',)
    fields = ('description', 'is_correct', 'course', 'unit', 'exam', 'question',)
    readonly_fields = ('course', 'unit', 'exam', 'question',)
    search_fields = ('description', )
    autocomplete_fields = ('question',)
    list_filter = ('question', 'is_correct',)
    
    def course(self, obj):
        return obj.question.exam.unit.course
    
    def unit(self, obj):
        return obj.question.exam.unit
    
    def exam(self, obj):
        return obj.question.exam
    
    def has_add_permission(self, request):
        return False
