from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Member(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

  def __str__(self):
      return (self.user.username)

class Venue(models.Model): 
  venue = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

  def __str__(self):
      return self.venue.username

class Event(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField()
  category = models.CharField(max_length=100)
  venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
  def __str__(self):
      return self.name

class Ticket(models.Model): 
  eventname = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event', to_field='name')
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='membertickets')
  forEvent = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventtickets')

  def __str__(self):
      return self.eventname.name

