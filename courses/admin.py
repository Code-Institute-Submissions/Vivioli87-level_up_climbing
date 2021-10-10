from django.contrib import admin
from .models import Level, CourseType, Course, Lesson, CourseLesson


# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'level',
        'name',
        'description'
    )


class CourseTypeAdmin(admin.ModelAdmin):
    list_display = (
        'level',
        'name',
        'description',
        'capacity',
        'price'
    )

    ordering = ('level',)


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'start_date',
        'level',
        'name',
    )

    ordering = ('start_date',)


admin.site.register(Level)
admin.site.register(CourseLesson)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Course, CourseAdmin)
