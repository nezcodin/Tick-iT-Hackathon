from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='home'),
    path('events/', views.events_view, name='events')
]