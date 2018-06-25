from django.contrib import admin

from alternatives.models import Alternative
from questions.models import Question


class AlternativeInlineModel(admin.TabularInline):
    model = Alternative


@admin.register(Question)    
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'statement', 'exam',)
    search_fields = ('statement',)
    autocomplete_fields = ('exam',)
    list_filter = ('exam',)
    inlines = [AlternativeInlineModel, ]
    
    def has_add_permission(self, request):
        return False

