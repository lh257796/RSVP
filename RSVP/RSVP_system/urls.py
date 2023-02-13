from django.urls import path
from . import views

app_name = 'RSVP_system'

# index shows a list of all venues
# event should show all events of the venue, and allow registration
# confirmed is the redirect that just shows confirmation of registration


urlpatterns = [
    path('', views.index, name='index'),
    # /RSVP/ is the index
    path('<int:venue_id>/', views.events, name='events'),
    # /RSVP/1 is the first venue, and contains a list of events
    path('<int:venue_id>/event/<int:event_id>/reservation', views.reservation, name='reservation'),
    # /RSVP/1/reservations is an event page, where users can input registration info
    path('<int:venue_id>/event/<int:event_id>/register', views.register, name='register'),
    path('<int:venue_id>/event/confirmation', views.confirmation, name='confirmation'),
]
