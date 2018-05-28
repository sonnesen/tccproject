from django.contrib import admin

from categories.models import Category


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Category, CategoryModelAdmin)
