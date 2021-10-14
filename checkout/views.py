from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import BookingForm
from courses.models import Course


def booking(request, course_id):
    """ Book a specific course """
    
    course = get_object_or_404(Course, pk=course_id)
    booking_form = BookingForm()
    template = 'checkout/booking.html'
    context = {
        'course': course,
        'booking_form': booking_form,
    }

    return render(request, template, context)