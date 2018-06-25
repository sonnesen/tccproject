from django.contrib import admin

from exams.models import Exam
from units.models import Unit
from videos.models import Video


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    verbose_name = 'Unit Video'
    verbose_name_plural = 'Unit Videos'
    

class ExamInline(admin.TabularInline):
    model = Exam
    extra = 1
    verbose_name = 'Unit Exam'
    verbose_name_plural = 'Unit Exams'    
    

@admin.register(Unit)
class UnitModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course',)
    autocomplete_fields = ('course',)
    search_fields = ('name',)
    list_filter = ('course',)
    inlines = [VideoInline, ExamInline]

    

