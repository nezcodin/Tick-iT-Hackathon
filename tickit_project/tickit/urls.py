from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('venues/', views.VenueList.as_view(), name='venue_list'),
    path('venues/<int:pk>/', views.VenueDetail.as_view(), name='venue-detail'),
    path('events/', views.EventList.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('tickets/', views.TicketList.as_view(), name='ticket_list'),
    path('tickets/<int:pk>/', views.TicketDetail.as_view(), name='ticket-detail')
]