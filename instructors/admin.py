from django.contrib import admin

from instructors.models import Instructor


@admin.register(Instructor)
class InstructorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'about',)
    search_fields = ('name',)


