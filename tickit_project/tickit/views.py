from django.shortcuts import render
from rest_framework import generics
from .models import Member, Venue, Event, Ticket
from .serializers import MemberSerializer, VenueSerializer, EventSerializer, TicketSerializer

# Site Views

def landing_view(request):
    return render(request, "home.html", {})

def event_details_view(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, "event_details.html", {'event': event})

def venue_details_view(request, pk):
    venue = Venue.objects.get(pk=pk)
    return render(request, "venue_details.html", {'venue': venue})

# API Views
class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer