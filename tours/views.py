import random
from django.shortcuts import render
from django.views.generic import View

from .data import title, subtitle, description, departures, tours


class MainView(View):
    # главная страница
    def get(self, request):
        random_tours = sorted(tours.items(), key=lambda x: random.random())[:6]
        context = {
            'title': title,
            'subtitle': subtitle,
            'description': description,
            'departures': departures,
            'tours': random_tours
        }
        return render(request, 'tours/index.html', context)


class TourView(View):
    # просмотр определенного тура
    def get(self, request, id):
        context = {
            'tour': tours[id],
            'departure': departures[tours[id]['departure']],
            'nights': tours[id]['nights'],
            'country': tours[id]['country'],
            'picture': tours[id]['picture'],
            'description': tours[id]['description'],
            'price': tours[id]['price'],
            'departures': departures,
        }
        return render(request, 'tours/tour.html', context)


class DepartureView(View):
    # выезд из определенного города
    def get(self, request, departure):
        # найдем все туры которые подходят по запросу departure=departure
        departure_tours = {}
        for key, tour in tours.items():
            if tour['departure'] == departure:
                departure_tours[key] = tour
        # создадим переменные и найдем туры с наименьшей и наибольшей ценой и
        # c наименьшим и наибольшим количеством дней в туре
        prices = []
        nights = []
        for min_tour in departure_tours.values():
            prices.append(min_tour['price'])
            nights.append(min_tour['nights'])
        min_price = min(prices)
        max_price = max(prices)

        min_nights = min(nights)
        max_nights = max(nights)
  
        context = {
            'departure': departures[departure],
            'tours': departure_tours,
            'departures': departures,
            'min_price': min_price,
            'max_price': max_price,
            'min_nights': min_nights,
            'max_nights': max_nights,
        }
        return render(request, 'tours/departure.html', context)
