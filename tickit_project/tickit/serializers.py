from rest_framework import serializers
from .models import Member, Venue, Event, Ticket

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    member = serializers.HyperlinkedRelatedField(
        view_name='member-detail',
        read_only=True
    )
    event = serializers.HyperlinkedRelatedField(
        view_name='event-detail',
        read_only=True
    )
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(),
        source='owner'
    )
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='forEvent'
    )
    class Meta:
       model = Ticket
       fields = ('id', 'eventname', 'owner', 'forEvent', 'owner_id', 'event_id', 'member', 'event')

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

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    ticket = serializers.HyperlinkedRelatedField(
        view_name='ticket-detail',
        many=True,
        read_only=True
    )
    member_url = serializers.ModelSerializer.serializer_url_field(
        view_name='member-detail'
    )
    class Meta:
       model = Member
       fields = ('id', 'member_url', 'ticket', 'identifier', 'email', 'first_name', 'last_name', 'password')