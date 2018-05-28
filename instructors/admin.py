from django.contrib import admin

from instructors.models import Instructor


class InstructorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'about')
    search_fields = ('name',)

    
admin.site.register(Instructor, InstructorModelAdmin)
