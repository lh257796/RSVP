from django.db import models

# Create your models here.

class Event(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# start, end time; venue

class Venue(models.Model):
    venue_name = models.CharField(max_length=45)

# name


class Reservation(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=45)

# first, last name, email


#events and venues created with admin page
#event viewing page with reservation functionality
