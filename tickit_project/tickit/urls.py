from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.MemberList.as_view(), name='member_list'),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name='member-detail'),
    path('venues/', views.VenueList.as_view(), name='venue_list'),
    path('venues/<int:pk>/', views.VenueDetail.as_view(), name='venue-detail'),
    path('events/', views.EventList.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('tickets/', views.TicketList.as_view(), name='ticket_list'),
    path('tickets/<int:pk>/', views.TicketDetail.as_view(), name='ticket-detail')
]