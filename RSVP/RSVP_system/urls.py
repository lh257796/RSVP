from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:venue_id>/', views.event, name='event'),
    # path('<int:venue_id>/events/<int:event_id>', views.reservation, name='reservation'),
    path('<int:venue_id>/confirmation', views.confirmation, name='confirmed'),
]
