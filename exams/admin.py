from django.contrib import admin
from django.contrib.admin.options import TabularInline, ModelAdmin
from django.urls.base import reverse
from django.utils.safestring import mark_safe

from exams.models import Exam
from questions.models import Question


class EditLinkToInlineObject(object):

    def edit_link(self, instance):
        url = reverse('admin:{0}_{1}_change'.format(
            instance._meta.app_label, 
            instance._meta.model_name), 
            args=[instance.pk])
        if instance.pk:
            return mark_safe('<a href="{0}">edit</a>'.format(url))
        else:
            return ''


class QuestionInline(EditLinkToInlineObject, TabularInline):
    model = Question
    verbose_name = 'Exam Question'
    verbose_name_plural = 'Exam Questions'
    readonly_fields = ('edit_link',)
    extra = 4
    
    def response_post_save_change(self, request, obj):
        pass


@admin.register(Exam)     
class ExamModelAdmin(ModelAdmin):
    list_display = ('title', 'unit',)
    search_fields = ('title',)
    autocomplete_fields = ('unit',)
    list_filter = ('unit',)
    inlines = [QuestionInline, ]

