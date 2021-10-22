from django.shortcuts import render, get_object_or_404

from .models import Course, CourseLesson
from checkout.models import Booking
from profiles.models import UserProfile
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
    profile = get_object_or_404(UserProfile, user=request.user)
    capacity = course.course_type.capacity

    course_bookings = Booking.objects.filter(booked_course=course).count()
    user_booked = Booking.objects.filter(booked_course=course, user_profile=profile)
    available_course_places = capacity - course_bookings

    print(user_booked)

    context = {
        'course': course,
        'course_lessons': course_lessons,
        'capacity':  capacity,
        'available_course_places': available_course_places,
        'user_booked': user_booked,
    }

    return render(request, 'courses/course_detail.html', context)
