from django.shortcuts import render

from .models import Course, CourseLesson
# Create your views here.


def all_courses(request):

    courses = Course.objects.all()
    course_lessons = CourseLesson.objects.all()

    context = {
        'courses': courses,
        'course_lessons': course_lessons,
    }

    return render(request, 'courses/courses.html', context)
