from django.contrib import admin
from .models import Subject
from teachers.admin import TeacherInline


def make_published(modeladmin, request, queryset):
    queryset.update(status='pd')

make_published.short_description = 'Make selected posts published'

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'update_at', 'status')
    ordering = ['name']
    search_fields = ('name', )
    list_filter = ('created_at', 'update_at')
    actions = [make_published]
    inlines = [TeacherInline]