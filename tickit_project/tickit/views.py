from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Venue, Event, Ticket
from .forms import RegistrationForm
from .serializers import UserSerializer, VenueSerializer, EventSerializer, TicketSerializer
from django.shortcuts import redirect
from django.contrib.auth import logout
import random

# Site Views

def landing_view(request):
    events = Event.objects.all()
    venues = Venue.objects.all()
    # Choose 10 random venues and events
    random_venues = random.sample(list(venues), k=8)
    random_events = random.sample(list(events), k=8)
    return render(request, "home.html", {'events': random_events, 'venues': random_venues})
    
def events_view(request):
    events = Event.objects.all()
    return render(request, "events.html", {'events': events})

def event_details_view(request, pk):
    event = Event.objects.get(pk=pk)
    tickets_available = random.randint(1, 150) # generate random number b/w 1-150
    return render(request, "event_details.html", {'event': event, 'tickets_available': tickets_available})

def venues_view(request):
    venues = Venue.objects.all()
    return render(request, "venues.html", {'venues': venues})

def venue_details_view(request, pk):
    venue = Venue.objects.get(pk=pk)
    events = Event.objects.all()
    return render(request, "venue_details.html", {'venue': venue, 'events': events})

def purchase_tickets_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    tickets = Ticket.objects.all()
    events = Event.objects.all()
    total_cost_tickets = sum(ticket.price for ticket in tickets)
    sales_tax = round(total_cost_tickets * 0.1, 2)
    total_cost_with_tax = round(total_cost_tickets + sales_tax, 2)
    return render(request, "tickets.html", {'tickets': tickets, 'events': events, 'event': event, 'total_cost_tickets': total_cost_tickets, 'sales_tax': sales_tax, 'total_cost_with_tax': total_cost_with_tax})

def thank_you_view(request):
    return render(request, "thank_you.html")

def login_view(request):
    return render(request, "login.html", {})

def logout_view(request):
    logout(request)
    return redirect('home')

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

class VenueDeleteView(DeleteView):
    model = Venue
    success_url = reverse_lazy('venues_list_view')

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