from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile, Coach
from checkout.models import Booking
from courses.models import Course

from .forms import UserProfileForm, CoachForm



def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    # check if user is a coach and display different profile/template
    if profile.is_coach:
        coach = get_object_or_404(Coach, coach=profile)

        if request.method == 'POST' and 'profile-info' in request.POST:
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')

        if request.method == 'POST' and 'coach-info' in request.POST:   
            coach_form = CoachForm(request.POST, request.FILES, instance=coach)
            if coach_form.is_valid():
                coach_form.save()
                messages.success(request, 'Coach information updated successfully')
        
        form = UserProfileForm(instance=profile)
        coach_form = CoachForm(instance=coach)
        course = Course.objects.all().order_by('start_date')
        coaches_courses = Course.objects.filter(coach=profile).order_by('start_date')

        template = 'profiles/coach_profile.html'
        context = {
            'form': form,
            'coach_form': coach_form,
            'profile': profile,
            'course': course,
            'coaches_courses': coaches_courses,
            'coach': coach,
        }

        return render(request, template, context)

    else:
        # return a normal user's profile page
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')

        form = UserProfileForm(instance=profile)
        bookings = Booking.objects.filter(user_profile=profile)
        course = Course.objects.all().order_by('start_date')

        template = 'profiles/profile.html'
        context = {
            'form': form,
            'profile': profile,
            'bookings': bookings,
            'course': course,
        }

        return render(request, template, context)
