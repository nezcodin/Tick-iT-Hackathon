from django.db import models
from django.conf import settings

class Venue(models.Model): 
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='member')
    name = models.CharField(max_length=100)
    location = models.TextField(default='location')

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    def __str__(self):
        return self.name

class Ticket(models.Model): 
    eventname = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='stuff', to_field='name')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usertickets')
    forEvent = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventtickets')

    def __str__(self):
        return self.eventname.name