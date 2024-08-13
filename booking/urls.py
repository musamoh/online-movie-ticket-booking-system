from django.urls import path
from .views import payment_gateway, payment_confirmation, reserve_seat,BookingListView,BookingDetailView\
,BookingDeleteView
app_name = 'booking'
urlpatterns = [
    path("seatchoice/<show_id>/", reserve_seat, name='reserve_seat'),
    path('payment/', payment_gateway, name='payment_gateway'),
    path('payment_confirmation/', payment_confirmation, name='payment_confirmation'),
    path('', BookingListView.as_view(), name='list'),
    path('<btid>/delete/', BookingDeleteView.as_view(), name='delete')
 ,   path('<btid>/', BookingDetailView.as_view(), name='detail'),
#    path(r'^(?P<btid>.*)/delete/$', BookingDeleteView.as_view(), name='delete')
]