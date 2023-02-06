from django.db import models

# Create your models here.

class Venue(models.Model):
    venue_name = models.CharField(max_length=45)

# name

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Event Start Time')
    end_time = models.DateTimeField('Event End Time')

# start, end time; venue



class Reservation(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=45)

# first, last name, email


#events and venues created with admin page
#event viewing page with reservation functionality
