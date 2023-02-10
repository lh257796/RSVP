from django.contrib import admin

# Register your models here.
from .models import Venue, Event, Reservation

# class ReservationInLine(admin.StackedInline):
#     model = Reservation
#     extra = 4

class EventInLine(admin.StackedInline):
    model = Event
    extra = 2
    # inlines = [ReservationInLine]

# class EventAdmin(admin.ModelAdmin):
#     inlines = [ReservationInLine]

class VenueAdmin(admin.ModelAdmin):
    fields = ['venue_name']
    inlines = [EventInLine]

admin.site.register(Venue, VenueAdmin)
admin.site.register(Event)
admin.site.register(Reservation)
