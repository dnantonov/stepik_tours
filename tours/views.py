from django.shortcuts import render
from django.views.generic import View

from .data import *


class MainView(View):
    def get(self, request):
        context = {
            'title': title,
            'subtitle': subtitle,
            'description': description,
            'departures': departures,
            'tours': tours
        }
        return render(request, 'tours/index.html', context)


class DepartureView(View):
    def get(self, request, departure):
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, id):
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

