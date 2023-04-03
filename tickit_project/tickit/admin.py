from django.contrib import admin
from django.contrib.auth.models import User
from .models import Venue, Event, Ticket

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Ticket)