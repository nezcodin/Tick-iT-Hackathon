from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Venue, Event, Ticket
from .forms import RegistrationForm
from .serializers import UserSerializer, VenueSerializer, EventSerializer, TicketSerializer
from django.shortcuts import redirect

# Site Views

def landing_view(request):
    events = Event.objects.all()
    venues = Venue.objects.all()
    return render(request, "home.html", {'events': events, 'venues': venues})
    
def events_view(request):
    events = Event.objects.all()
    return render(request, "events.html", {'events': events})

def event_details_view(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, "event_details.html", {'event': event})

def venues_view(request):
    venues = Venue.objects.all()
    return render(request, "venues.html", {'venues': venues})

def venue_details_view(request, pk):
    venue = Venue.objects.get(pk=pk)
    events = Event.objects.all()
    return render(request, "venue_details.html", {'venue': venue, 'events': events})

def login_view(request):
    return render(request, "login.html", {})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Full Create, Update, and Delete Views

class VenueCreateView(CreateView):
    model = Venue
    template_name = 'create_venue.html'
    fields = ['name', 'location', 'photo_url']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Set the owner of the Venue to the logged-in user
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        if self.object:
            # Redirect to the details view of the created Venue
            return redirect('venue_details_view', pk=self.object.pk)
        else:
            # Handle error if Venue object was not created
            return ('there was an error creating the venue')
    
class VenueUpdateView(UpdateView):
    model = Venue
    template_name = 'update_venue.html'
    fields = ['name', 'location', 'photo_url']
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.object:
            # Redirect to the details view of the created Venue
            return redirect('venue_details_view', pk=self.object.pk)
        else:
            # Handle error if Venue object was not created
            return ('there was an error updating the venue')

class VenueDeleteView(generics.DestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

# REST API Views
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