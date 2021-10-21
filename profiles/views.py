from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from checkout.models import Booking
from courses.models import Course


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    bookings = Booking.objects.filter(user_profile=profile)
    course = Course.objects.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'bookings': bookings,
        'course': course,
    }

    return render(request, template, context)
