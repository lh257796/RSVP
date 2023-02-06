from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
# from django.template import loader
from django.shortcuts import render
from .models import Venue


# Create your views here.

def index(request):
    all_venues = Venue.objects.order_by()
    # template = loader.get_template('RSVP_system/index.html')
    context = {
        'all_venues': all_venues
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'RSVP_system/index.html', context)

# event viewing page with reservation functionality
def event(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    return render(request, 'RSVP_system/event.html', {'venue':venue})

def confirmed(request, venue_id):
    response = "Confirmed your reservation for %s"
    return HttpResponse(response % venue_id)
