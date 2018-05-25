from django.contrib import admin
from django.contrib.admin.options import TabularInline, ModelAdmin
from django.forms.models import ModelForm

from exams.models import Exam
from questions.models import Question


# from alternatives.models import Alternative
# class AlternativeInline(NestedTabularInline):
#     model = Alternative
#     verbose_name = 'Question Alternative'
#     verbose_name_plural = 'Question Alternatives'
# 
#     
class QuestionInline(TabularInline):
    model = Question
    verbose_name = 'Exam Question'
    verbose_name_plural = 'Exam Questions'
     
     
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'unit', 'course']

     
class ExamModelAdmin(ModelAdmin):
    list_display = ('title', 'unit',)
    search_fields = ('title',)
    autocomplete_fields = ('unit',)
    list_filter = ('unit',)
    inlines = [QuestionInline, ]
    form = ExamForm
 
admin.site.register(Exam, ExamModelAdmin)
