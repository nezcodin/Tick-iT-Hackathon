from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='home'),
    path('events/<int:pk>/', views.event_details_view, name='event_details_view'),
    path('venues/<int:pk>/', views.venue_details_view, name='venue_details_view'),
    path('events/', views.events_view, name='events'),
    path('register/', views.registration, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
]

