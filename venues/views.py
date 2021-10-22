from django.shortcuts import render
from .models import Venue

# Create your views here.


def all_venues(request):

    venues = Venue.objects.all()

    context = {
        'venues': venues,
    }

    return render(request, 'venues/venues.html', context)
