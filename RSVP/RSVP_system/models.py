from django.db import models

# Create your models here.

class Venue(models.Model):
    venue_name = models.CharField(max_length=45)
    def __str__(self):
        return self.venue_name
# name

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    start_time = models.TimeField('Event Start Time')
    end_time = models.TimeField('Event End Time')
    def __str__(self):
        return '%s: %s - %s' % (self.name, self.start_time, self.end_time)

# start, end time; venue



class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=45)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
# first, last name, email


#events and venues created with admin page
#event viewing page with reservation functionality
