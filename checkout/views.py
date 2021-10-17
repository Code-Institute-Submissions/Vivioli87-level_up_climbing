from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import BookingForm
from .models import Booking
from courses.models import Course

import stripe


def booking(request, course_id):
    """ Book a specific course """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    course = get_object_or_404(Course, pk=course_id)
    course_name = course.name
    course_price = course.course_type.price

    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        course_price = course.course_type.price

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'booking_total': course_price,
            'booked_course': course_name,
        }

        booking_form = BookingForm(form_data)

        if booking_form.is_valid():
            booking_submission = booking_form.save()
            
            return redirect(reverse('booking_success',
                                    args=[booking_submission.booking_reference]))
        # else:
        #     messages.error(request, 'There was an error on the booking form')

    else:
        stripe_total = round(course_price * 100)
        stripe.api_key = stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        booking_form = BookingForm()

    template = 'checkout/booking.html'
    context = {
        'course': course,
        'booking_form': booking_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template,
                  context)


def booking_success(request, booking_reference):

    # save_info = request.session.get('save_info')

    booking_submission = get_object_or_404(Booking, 
                                           booking_reference=booking_reference)
    messages.success(request,
                     f'Booking successfully processes! {booking_reference}')

    template = 'checkout/booking_success.html'
    context = {
        'booking_submission': booking_submission,
    }

    return render(request, template,
                  context)
