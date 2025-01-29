from django.contrib import admin
from .models import Teacher


class TeacherInline(admin.StackedInline):
    model = Teacher
    extra = 1

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject', 'email', 'created_at')
    search_fields = ['first_name', 'last_name']
    prepopulated_fields = {'email':  ('first_name',)}
    readonly_fields = ('created_at', 'update_at')
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Main Information', {
            'fields': ('first_name', 'last_name', 'subject', 'email', 'phone', 'image')
        }),
        ('Additional Information',{
            'fields': ('work_experience', 'created_at', 'update_at'),
        }),
    )

