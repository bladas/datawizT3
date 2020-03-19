from django.urls import NoReverseMatch
from rest_framework import serializers


from .models import *

from rest_framework.relations import HyperlinkedIdentityField


class AircraftsDataListSerializer(serializers.ModelSerializer):

    url = HyperlinkedIdentityField(view_name='aircraftsdata-detail')

    class Meta:
        model = AircraftsData
        fields = ('aircraft_code', 'model', 'range', 'url')


class AircraftsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftsData
        fields = ('aircraft_code', 'model', 'range')


class AirportsDataListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='airportsdata-detail')

    class Meta:
        model = AirportsData
        fields = ('airport_code', 'airport_name', 'city', 'coordinates', 'timezone', 'url')


class AirportsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportsData
        fields = ('airport_code', 'airport_name', 'city', 'coordinates', 'timezone')


class BoardingPassesHyperlinkIdentityField(HyperlinkedIdentityField):
    def get_url(self, *args):
        url = super().get_url(*args)
        # print(url[:-1])
        true_url = url[:-1]
        getpk = str(args[0]).split()
        ez = getpk[-1]

        return true_url + "&" + ez + "/"


class BoardingPassesListSerializer(serializers.ModelSerializer):
    url = BoardingPassesHyperlinkIdentityField(view_name='boardingpasses-detail', read_only=True)

    class Meta:
        model = BoardingPasses
        fields = ('ticket_no', 'flight_id', 'boarding_no', 'seat_no', 'url')


class BoardingPassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardingPasses
        fields = ('ticket_no', 'flight_id', 'boarding_no', 'seat_no')


class BookingsListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='bookings-detail')

    class Meta:
        model = Bookings
        fields = ('book_ref', 'book_date', 'total_amount', 'url')


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ('book_ref', 'book_date', 'total_amount')


class FlightsListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='flights-detail')

    class Meta:
        model = Flights
        fields = ('flight_id', 'flight_no', 'scheduled_departure', 'scheduled_arrival',
                  'departure_airport', 'arrival_airport', 'status', 'aircraft_code', 'actual_departure',
                  'actual_arrival', 'url')


class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = ('flight_id', 'flight_no', 'scheduled_departure', 'scheduled_arrival',
                  'departure_airport', 'arrival_airport', 'status', 'aircraft_code', 'actual_departure',
                  'actual_arrival')


class SeatsHyperlinkIdentityField(HyperlinkedIdentityField):
    def get_url(self, *args):
        url = super().get_url(*args)
        print(url[:-1])
        true_url = url[:-1]
        print(args)
        getpk = str(args[0]).split()
        ez = getpk[-1]

        return true_url + "&" + ez + "/"


class SeatsListSerializer(serializers.ModelSerializer):
    url = SeatsHyperlinkIdentityField(view_name='seats-detail', read_only=True)

    class Meta:
        model = Seats
        fields = ('aircraft_code', 'seat_no', 'fare_conditions', 'url')


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ('aircraft_code', 'seat_no', 'fare_conditions')


class TicketFlightsHyperlinkIdentityField(HyperlinkedIdentityField):
    def get_url(self, *args):
        url = super().get_url(*args)
        # print(url[:-1])
        true_url = url[:-1]
        getpk = str(args[0]).split()
        ez = getpk[-1]

        return true_url + "&" + ez + "/"


class TicketFlightsListSerializer(serializers.ModelSerializer):
    url = TicketFlightsHyperlinkIdentityField(view_name='ticketflights-detail', read_only=True)

    class Meta:
        model = TicketFlights
        fields = ('ticket_no', 'flight', 'fare_conditions', 'amount', 'url')


class TicketFlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketFlights
        fields = ('ticket_no', 'flight', 'fare_conditions', 'amount')


class TicketsListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='tickets-detail', read_only=True)

    class Meta:
        model = Tickets
        fields = ('ticket_no', 'book_ref', 'passenger_id', 'passenger_name', 'contact_data', 'url')


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('ticket_no', 'book_ref', 'passenger_id', 'passenger_name', 'contact_data')
