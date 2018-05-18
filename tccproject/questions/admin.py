from django.contrib import admin

from questions.models import Question


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'statement', 'exam',)
    search_fields = ('statement',)
    autocomplete_fields = ('exam',)
    list_filter = ('exam',)


admin.site.register(Question, QuestionModelAdmin)
