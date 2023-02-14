from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import render
from .models import Venue, Event, Reservation
from django.urls import reverse

# for class-based templates
from django.views.generic import TemplateView, ListView
from django.views import View


# Create your views here.


#index: contains a list of all venues, when clicked goes to /RSVP/<venue_id>
#---function index view
# def index(request):
#     all_venues = Venue.objects.order_by()
#     # template = loader.get_template('RSVP_system/index.html')
#     context = {
#         'all_venues': all_venues
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'RSVP_system/index.html', context)
#---

# event viewing page with reservation functionality
# this is a venue page. it should contain a radio option set of events
# to choose from. then, a first, last name + email can be used to reserve
#---CLASS-BASED INDEX VIEW

class Index(View):
    def get(self, request):
        all_venues = Venue.objects.order_by()
        context = {
            'all_venues': all_venues
        }
        return render(request, 'RSVP_system/index.html', context)
#---

def events(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    all_events = Event.objects.order_by()
    events = []
    for event in all_events:
        if event.venue_id == venue_id:
            events.append(event)
    context = {
        'events': events,
        'venue': venue
    }
    return render(request, 'RSVP_system/events.html', context)

#---CLASS-BASED EVENTS VIEW ATTEMPT

# class Events(ListView):
#     def get(self, request, venue_id):
#         venue = get_object_or_404(Venue, pk=venue_id)
#         all_events = Event.objects.order_by()
#         events = []
#         for event in all_events:
#             if event.venue_id == venue_id:
#                 events.append(event)
#         context = {
#             'events': events,
#             'venue': venue
#         }
#         return render(request, 'RSVP_system/classevents.html', context)


#---

# reservation: should be able to give a form, post to the register view
# and should then redirect to confirmation
# separate css as well

def reservation(request, venue_id, event_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'venue': venue,
        'event': event
    }
    # this is the problem: the render results in a NoReverseMatch error
    # what is happening is that multiple events are being rendered and the reservation.html tempplate
    # was NOT accounting for this.
    # I need to get specific event ids and pass them on
    return render(request, 'RSVP_system/reservation.html', context)

#---CLASS-BASED RESERVATION VIEW



#---
# confirmation should either fail and render event page again, or success and
# redirect
def register(request, venue_id, event_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    try:
        selected_event = venue.event_set.get(pk=event_id)
        print('GOT SELECTED_EVENT', selected_event)
        # experiment here?
        # create a reservation
    except (KeyError, Event.DoesNotExist):
        #display form again
        return render(request, 'RSVP_system/event.html', {
            'venue':venue,
            'error_message': "Please select an event and try again."
        })
    Reservation.objects.create(
        event=selected_event,
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        )
    rezy = Reservation.objects.order_by()
    print('LIST OF RESERVATIONS NOW', rezy)

    # success = "Confirmed your reservation for %s"
    # always return redirect when POST successful
    return HttpResponseRedirect(reverse('RSVP_system:confirmation', args=(venue.id,)))
    # return render(request, 'RSVP_system/event.html', {'venue':venue})

    #---CLASS-BASED REGISTER VIEW







#---


def confirmation(request, venue_id):
    response = "Confirmed your reservation for %s! You can now close this page."
    venue = get_object_or_404(Venue, pk=venue_id)
    return HttpResponse(response % venue)


#---CLASS-BASED CONFIRMATION VIEW







#---

# check how to import CSS libraries into django (bootstrap, tailwind)
    # (there are best practices, ie in two scoops)
