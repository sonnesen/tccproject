from django.contrib import admin
from django.contrib.admin.options import TabularInline, ModelAdmin
from django.urls.base import reverse
from django.utils.safestring import mark_safe

from courses.models import Course, Document, Video, Unit, Question, Exam, \
    Alternative, Instructor, Category


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


class UnitInline(EditLinkToInlineObject, TabularInline):
    model = Unit
    readonly_fields = ('edit_link',)
    verbose_name = 'Course Unit'
    verbose_name_plural = 'Course Units'

    
class QuestionInline(EditLinkToInlineObject, TabularInline):
    model = Question
    verbose_name = 'Exam Question'
    verbose_name_plural = 'Exam Questions'
    readonly_fields = ('edit_link',)
    extra = 4
    
    def response_post_save_change(self, request, obj):
        pass


class DocumentInLine(TabularInline):
    model = Document
    extra = 1
    verbose_name = 'Unit Document'
    verbose_name_plural = 'Unit Documents'

    
class VideoInline(TabularInline):
    model = Video
    extra = 1
    verbose_name = 'Unit Video'
    verbose_name_plural = 'Unit Videos'
    

class ExamInline(EditLinkToInlineObject, TabularInline):
    model = Exam
    extra = 1
    readonly_fields = ('edit_link',)
    verbose_name = 'Unit Exam'
    verbose_name_plural = 'Unit Exams'


class AlternativeInline(TabularInline):
    model = Alternative
    extra = 4


@admin.register(Course)    
class CourseModelAdmin(ModelAdmin):
    list_display = ('name', 'created_at', 'category', 'instructor',
                    'keyword_list', 'description', 'image',)
    autocomplete_fields = ('category', 'instructor',)
    readonly_fields = ('created_at',)
    list_filter = ('name', 'category', 'instructor',)
    search_fields = ('name', 'category', 'instructor',)
    inlines = [UnitInline, ]
    
    def get_queryset(self, request):
        return super(
            CourseModelAdmin, self).get_queryset(
                request).prefetch_related('keywords')

    def keyword_list(self, obj):
        return ", ".join(o.name for o in obj.keywords.all())

    
@admin.register(Document)
class DocumentModelAdmin(ModelAdmin):
    list_display = ('name', 'file', 'unit', 'course')
    search_fields = ('name',)
    autocomplete_fields = ('unit',)
    list_filter = ('name',)
    
    def course(self, obj):
        return obj.unit.course


@admin.register(Video)
class VideoModelAdmin(ModelAdmin):
    list_display = ('name', 'embedded', 'file', 'unit', 'course')
    search_fields = ('name',)
    autocomplete_fields = ('unit',)
    list_filter = ('name',)
    
    def course(self, obj):
        return obj.unit.course

    
@admin.register(Exam)     
class ExamModelAdmin(ModelAdmin):
    list_display = ('title', 'unit', 'course',)
    fields = ('title', 'unit', 'course',)
    readonly_fields = ('course',)
    search_fields = ('title',)
    autocomplete_fields = ('unit',)
    list_filter = ('unit',)
    inlines = [QuestionInline]
    
    def course(self, obj):
        return obj.unit.course
    
    course.short_description = 'Course'
    course.admin_order_field = 'unit__course'    
    

@admin.register(Unit)
class UnitModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'course',)
    autocomplete_fields = ('course',)
    search_fields = ('name',)
    list_filter = ('course',)
    inlines = [VideoInline, ExamInline, DocumentInLine, ]    


@admin.register(Question)    
class QuestionModelAdmin(ModelAdmin):
    list_display = ('id', 'statement', 'exam', 'unit', 'course',)
    search_fields = ('statement',)
    autocomplete_fields = ('exam',)
    list_filter = ('exam',)
    inlines = [AlternativeInline, ]
    
    def unit(self, obj):
        return obj.exam.unit
    
    def course(self, obj):
        return obj.exam.unit.course
    
    
@admin.register(Instructor)
class InstructorModelAdmin(ModelAdmin):
    list_display = ('name', 'contact', 'about',)
    search_fields = ('name',)    

    
@admin.register(Alternative)
class AlternativeModelAdmin(ModelAdmin):
    list_display = ('description', 'is_correct', 'course', 'unit', 'exam', 'question',)
    fields = ('description', 'is_correct', 'course', 'unit', 'exam', 'question',)
    readonly_fields = ('course', 'unit', 'exam', 'question',)
    search_fields = ('description',)
    autocomplete_fields = ('question',)
    list_filter = ('question', 'is_correct',)
    
    def course(self, obj):
        return obj.question.exam.unit.course
    
    def unit(self, obj):
        return obj.question.exam.unit
    
    def exam(self, obj):
        return obj.question.exam
    
    
@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
