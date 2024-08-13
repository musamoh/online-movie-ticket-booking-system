from django.urls import path
from .views import TheatreListView, theatre_details
app_name = 'theatre'
urlpatterns = [
    path('', TheatreListView.as_view(), name='list'),
    path('<theatre_id>/', theatre_details, name='detail')
]