from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from django.conf import settings
from .models import Venue, Event, Ticket
from .forms import RegistrationForm
from .serializers import UserSerializer, VenueSerializer, EventSerializer, TicketSerializer

# Site Views

def landing_view(request):
    return render(request, "home.html", {})
    
def event_details_view(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, "event_details.html", {'event': event})

def venue_details_view(request, pk):
    venue = Venue.objects.get(pk=pk)
    events = Event.objects.all()
    return render(request, "venue_details.html", {'venue': venue, 'events': events})

def events_view(request):
    return render(request, "events.html", {})

def login_view(request):
    return render(request, "login.html", {})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# API Views
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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