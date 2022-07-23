from django.urls import path

from . import views

urlpatterns = [
    path('airport', views.airport_api_overview, name='airport'),
    path('flight', views.flight_api_overview, name='flight'),
]
