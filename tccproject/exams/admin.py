from django.contrib import admin

from exams.models import Exam


class ExamModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'unit',)
    search_fields = ('title',)
    autocomplete_fields = ('unit',)
    list_filter = ('unit',)


admin.site.register(Exam, ExamModelAdmin)
