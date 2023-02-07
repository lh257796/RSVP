from django.urls import path
from . import views

app_name = 'RSVP_system'

# index shows a list of all venues
# event should show all events of the venue, and allow registration
# confirmed is the redirect that just shows confirmation of registration


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:venue_id>/', views.event, name='event'),
    path('<int:venue_id>/reservation', views.event, name='event'),
    path('<int:venue_id>/confirmation', views.confirmation, name='confirmation'),
]
