from django.urls import path

# from .views import MainView, DepartureView, TourView
from .views import index, departure_view, tour_view

urlpatterns = [
    # path('', MainView.as_view()),
    # path('departure/<str:departure>/', DepartureView.as_view()),
    # path('tour/<int:id>/', TourView.as_view()),
    path('', index, name="index"),
    path('departure/<str:departure>/', departure_view, name="departure"),
    path('tour/<int:id>/', tour_view, name="tour"),
]