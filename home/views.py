from django.shortcuts import render

from venues.models import Venue


def index(request):
    return render(request, 'home/index.html')


def about(request):

    venues = Venue.objects.all()

    context = {
        'venues': venues,
    }

    return render(request, 'home/about.html', context)
