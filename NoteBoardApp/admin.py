from django.contrib import admin
from .models import Category, Note


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'is_active')
    list_display_links = ('name',)
    list_filter = ('color', 'is_active')
    list_editable = ('color', 'is_active')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline', 'is_done', )
    list_filter = ('is_done', )
