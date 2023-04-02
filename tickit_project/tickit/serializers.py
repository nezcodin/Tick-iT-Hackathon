from rest_framework import serializers
from .models import User, Venue, Event, Ticket

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    event = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event'
    )
    class Meta:
       model = Ticket
       fields = ('id', 'eventname', 'userId', 'eventId', 'user_id', 'event_id', 'user', 'event')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )
    ticket = serializers.HyperlinkedRelatedField(
        view_name='ticket_detail',
        many=True,
        read_only=True
    )
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )
    event_url = serializers.ModelSerializer.serializer_url_field(
        view_name='event_detail'
    )
    class Meta:
       model = Event
       fields = ('id', 'event_url', 'name', 'description', 'category', 'venueId', 'venue_id', 'venue', 'ticket')

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail'
    )
    class Meta:
       model = Venue
       fields = ('id', 'venue_url', 'name', 'username', 'password', 'address', 'event')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    ticket = serializers.HyperlinkedRelatedField(
        view_name='ticket_detail',
        many=True,
        read_only=True
    )
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )
    class Meta:
       model = User
       fields = ('id', 'user_url', 'name', 'username', 'password', 'ticket')