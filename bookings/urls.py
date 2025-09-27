from django.urls import path
from . import views

urlpatterns = [
    path('confirm/', views.booking_confirm, name='booking_confirm'),
    path('payment/', views.process_payment, name='process_payment'),
    path('ticket/<uuid:booking_id>/', views.ticket_view, name='ticket_view'),
    path('download/<uuid:booking_id>/', views.download_ticket, name='download_ticket'),
]