from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)

  def __str__(self):
      return self.name

class Venue(models.Model): 
  name = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  address = models.TextField()

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
  eventname = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event', to_field='name')
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usertickets')
  forEvent = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventtickets')

  def __str__(self):
      return self.eventname.name
