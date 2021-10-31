from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import Course, CourseLesson, Level
from checkout.models import Booking
from profiles.models import UserProfile

from .forms import CourseForm
# Create your views here.


def all_courses(request):
    """ A view to bring back all active courses,
    paginated. Include filter on course level"""

    courses = Course.objects.filter(course_complete=False).order_by('start_date')

    levels = None

    if request.GET:
        if 'level' in request.GET:
            levels = request.GET['level'].split(',')
            courses = courses.filter(level__name__in=levels)
            levels = Level.objects.filter(name__in=levels)

            page = request.GET.get('page', 1)
            paginator = Paginator(courses, 3)

            try:
                courses = paginator.page(page)
            except PageNotAnInteger:
                courses = paginator.page(1)
            except EmptyPage:
                courses = paginator.page(paginator.num_pages)
    else:
        page = request.GET.get('page', 1)
        paginator = Paginator(courses, 3)

        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)

    context = {
        'courses': courses,
        'levels': levels,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """A view to show individual course details """

    course = get_object_or_404(Course, pk=course_id)
    course_lessons = CourseLesson.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)
    capacity = course.course_type.capacity

    course_bookings = Booking.objects.filter(booked_course=course).count()
    user_booked = Booking.objects.filter(booked_course=course,
                                         user_profile=profile)
    available_course_places = capacity - course_bookings

    context = {
        'course': course,
        'course_lessons': course_lessons,
        'capacity':  capacity,
        'available_course_places': available_course_places,
        'user_booked': user_booked,
    }

    return render(request, 'courses/course_detail.html', context)


@login_required
def add_course(request):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Successfully added course!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(request,
                           ('Failed to add course. '
                            'Please ensure the form is valid.'))
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_course(request, course_id):
    """
    Edit a course
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you do not have permissions to do that.')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Successfully edited the course!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(request,
                           ('Failed to edit course. '
                            'Please ensure the form is valid.'))
    else:
        form = CourseForm(instance=course)

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)
