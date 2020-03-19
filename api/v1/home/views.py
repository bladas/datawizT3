import jwt
from django.contrib.auth import user_logged_in
from rest_framework import viewsets, permissions, decorators, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler

from .models import *
from .serializers import *


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """

    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class AircraftsDataView(viewsets.ModelViewSet):
    queryset = AircraftsData.objects.all()
    serializer_class = AircraftsDataListSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = AircraftsDataSerializer(instance)
        return Response(serializer.data)


class AirportsDataView(viewsets.ModelViewSet):
    queryset = AirportsData.objects.all()
    serializer_class = AirportsDataListSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }
    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = AirportsDataSerializer(instance)
        return Response(serializer.data)


class BoardingPassesView(viewsets.ModelViewSet):
    queryset = BoardingPasses.objects.all()
    serializer_class = BoardingPassesListSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }
    def retrieve(self, request, *args, **kwargs):
        full_pk = str(kwargs.get('pk'))

        l = full_pk.split('&')
        pk = l[0]
        flight = l[1]
        instance = get_object_or_404(self.queryset, pk=pk, flight_id=flight)
        serializer = BoardingPassesSerializer(instance)
        return Response(serializer.data)


class BookingsView(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsListSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }
    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = BookingsSerializer(instance)
        return Response(serializer.data)


class FlightsView(viewsets.ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightsListSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }
    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = FlightsSerializer(instance)
        return Response(serializer.data)


class SeatsView(viewsets.ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = SeatsListSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }
    def retrieve(self, request, *args, **kwargs):
        full_pk = str(kwargs.get('pk'))

        l = full_pk.split('&')
        pk = l[0]
        seat_no = l[1]
        instance = get_object_or_404(self.queryset, pk=pk, seat_no=seat_no)
        serializer = SeatsSerializer(instance)
        return Response(serializer.data)


class TicketFlightsView(viewsets.ModelViewSet):
    queryset = TicketFlights.objects.all()
    serializer_class = TicketFlightsListSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }
    def retrieve(self, request, *args, **kwargs):

        # do your customization here
        # print(self.request)
        full_pk = str(kwargs.get('pk'))
        try:
            l = full_pk.split('&')
            pk = l[0]
            flight = l[1]
            print(pk)
            print(flight)
            print("1")
            print(self.queryset.filter(pk=kwargs.get('pk')))
            print(self.request.parser_context)
            print(self.kwargs)
            # print(str(TicketFlights.objects.filter(pk=kwargs.get('pk'))[0]).split()[-1])
            print(TicketFlights.objects.filter(pk=pk, flight=flight))
            # instance = self.get_object()
            queryset = TicketFlights.objects.all()
            instance = get_object_or_404(queryset, pk=pk, flight=flight)
            print(instance)
            serializer = TicketFlightsSerializer(instance)

        except:
            print(full_pk)
            instance = TicketFlights.objects.filter(pk=full_pk)
            serializer = TicketFlightsSerializer(instance)
        return Response(serializer.data)


class TicketsView(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsListSerializer
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        AllowAny: ['retrieve']
    }
    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = TicketsSerializer(instance)
        return Response(serializer.data)
