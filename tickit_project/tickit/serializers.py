from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Venue, Event, Ticket

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True
    )
    event = serializers.HyperlinkedRelatedField(
        view_name='event-detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='owner'
    )
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='forEvent'
    )
    class Meta:
       model = Ticket
       fields = ('id', 'eventname', 'owner', 'forEvent', 'user_id', 'event_id', 'user', 'event')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue-detail',
        read_only=True
    )
    ticket = serializers.HyperlinkedRelatedField(
        view_name='ticket-detail',
        many=True,
        read_only=True
    )
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )
    event_url = serializers.ModelSerializer.serializer_url_field(
        view_name='event-detail'
    )
    class Meta:
       model = Event
       fields = ('id', 'event_url', 'name', 'description', 'category', 'venue', 'venue_id', 'venue', 'ticket')

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(
        view_name='event-detail',
        many=True,
        read_only=True
    )
    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue-detail'
    )
    class Meta:
       model = Venue
       fields = ('id', 'venue_url', 'name', 'username', 'password', 'address', 'event')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    ticket = serializers.HyperlinkedRelatedField(
        view_name='ticket-detail',
        many=True,
        read_only=True
    )
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user-detail'
    )
    class Meta:
       model = User
       fields = ('id', 'user_url', 'name', 'username', 'password', 'ticket')