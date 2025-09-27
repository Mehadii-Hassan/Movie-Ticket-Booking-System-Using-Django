from django.contrib import admin
from .models import Booking, BookedSeat, Payment

class BookedSeatInline(admin.TabularInline):
    model = BookedSeat
    extra = 0

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'user', 'showtime', 'total_amount', 'payment_status', 'booking_date']
    list_filter = ['payment_status', 'booking_date']
    search_fields = ['booking_id', 'user__username']
    inlines = [BookedSeatInline]
    readonly_fields = ['booking_id']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'booking', 'payment_method', 'amount', 'payment_date']
    list_filter = ['payment_method', 'payment_date']
    search_fields = ['transaction_id', 'booking__booking_id']