from django.shortcuts import render

from venues.models import Venue
from profiles.models import Coach


def index(request):
    return render(request, 'home/index.html')


def about(request):

    venues = Venue.objects.all()
    coaches = Coach.objects.all()

    context = {
        'venues': venues,
        'coaches': coaches,
    }

    return render(request, 'home/about.html', context)
