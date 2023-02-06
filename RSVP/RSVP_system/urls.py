from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:venue_id>/', views.event, name='event'),
    path('<int:venue_id>/confirmed', views.confirmed, name='confirmed'),
]
