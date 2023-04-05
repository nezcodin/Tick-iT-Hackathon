from django.contrib import admin
from .models import Venue, Event, Ticket
from django.contrib.auth import get_user_model

User = get_user_model()

# admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Ticket)