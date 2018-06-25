from django.contrib import admin

from categories.models import Category

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
