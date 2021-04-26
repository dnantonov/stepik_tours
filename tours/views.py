from django.shortcuts import render
from django.views.generic.base import TemplateView

from .data import *


def index(request):
    context = {
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'departures': departures,
        'tours': tours
    }
    return render(request, 'tours/index.html', context)


def departure_view(request, departure):
    return render(request, 'tours/departure.html')


def tour_view(request, id):
    tour = tours[id]
    departure = departures[tours[id]['departure']]
    nights = tours[id]['nights']
    country = tours[id]['country']
    picture = tours[id]['picture']
    description = tours[id]['description']
    price = tours[id]['price']

    context = {
        'tour': tour,
        'departure': departure,
        'nights': nights,
        'country': country,
        'picture': picture,
        'description': description,
        'price': price
    }

    return render(request, 'tours/tour.html', context)



# class MainView(TemplateView):
#     template_name = 'tours/index.html'
#
#
# class DepartureView(TemplateView):
#     template_name = 'tours/departure.html'
#
#
# class TourView(TemplateView):
#     template_name = 'tours/tour.html'

