from django.shortcuts import render, get_object_or_404

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


def course_detail(request, course_id):
    """A view to show individual course details """

    course = get_object_or_404(Course, pk=course_id)
    course_lessons = CourseLesson.objects.all()

    context = {
        'course': course,
        'course_lessons': course_lessons,
    }

    return render(request, 'courses/course_detail.html', context)
