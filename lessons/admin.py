from django.contrib import admin
from .models import Level, Lesson

# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'level',
        'name',
        'description'
    )

    ordering = ('level',)

admin.site.register(Level)
admin.site.register(Lesson, LessonAdmin)
