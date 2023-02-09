from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import render
from .models import Venue, Event, Reservation
from django.urls import reverse


# Create your views here.


#index: contains a list of all venues, when clicked goes to /RSVP/<venue_id>
def index(request):
    all_venues = Venue.objects.order_by()
    # template = loader.get_template('RSVP_system/index.html')
    context = {
        'all_venues': all_venues
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'RSVP_system/index.html', context)

# event viewing page with reservation functionality
# this is a venue page. it should contain a radio option set of events
# to choose from. then, a first, last name + email can be used to reserve


#event: should show JUST a list of reservations, that's it!!
def event(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    return render(request, 'RSVP_system/event.html', {'venue':venue})

# def reservation(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     return render(request, 'RSVP_system/reservation.html', {'event':event})


# confirmation should either fail and render event page again, or success and
# redirect
def register(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    try:
        selected_event = venue.event_set.get(pk=request.POST['event'])
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
    success = "Confirmed your reservation for %s"
    # always return redirect when POST successful
    return HttpResponseRedirect(reverse('RSVP_system:confirmation', args=(venue.id,)))
    # return render(request, 'RSVP_system/event.html', {'venue':venue})


def confirmation(request, venue_id):
    response = "Confirmed your reservation for %s! You can now close this page."
    venue = get_object_or_404(Venue, pk=venue_id)
    return HttpResponse(response % venue)
