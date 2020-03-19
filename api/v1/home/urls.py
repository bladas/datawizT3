from django.urls import path, include
from . import views
from api.v1.user.views import registration
from rest_framework import routers

router = routers.DefaultRouter()

router.register('AircraftsData', views.AircraftsDataView)
router.register('AirportsData', views.AirportsDataView)
router.register('BoardingPasses', views.BoardingPassesView)

router.register('Bookings', views.BookingsView)
router.register('Flights', views.FlightsView)
router.register('Seats', views.SeatsView)
router.register('TicketFlights', views.TicketFlightsView)
router.register('Tickets', views.TicketsView)

urlpatterns = [
    path('', include(router.urls)),

]

#
# def print_url_pattern_names(patterns):
#     """Print a list of urlpattern and their names"""
#     for pat in patterns:
#         if pat.__class__.__name__ == 'URLResolver':  # load patterns from this URLResolver
#             print_url_pattern_names(pat.url_patterns)
#         elif pat.__class__.__name__ == 'URLPattern':  # load name from this URLPattern
#             if pat.name is not None:
#                 print('[API-URL] {:>50} -> {}'.format(pat.name, pat.pattern))
# print_url_pattern_names(urlpatterns)