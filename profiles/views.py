from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile, Coach
from checkout.models import Booking
from courses.models import Course

from .forms import UserProfileForm



def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    
    form = UserProfileForm(instance=profile)
    bookings = Booking.objects.filter(user_profile=profile)
    coach = Coach.objects.all()
    course = Course.objects.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'bookings': bookings,
        'course': course,
        'coach': coach,
    }

    return render(request, template, context)
