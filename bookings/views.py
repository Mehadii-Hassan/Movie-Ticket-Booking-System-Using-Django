from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Booking, BookedSeat, Payment
from movies.models import ShowTime, Seat
import uuid
from decimal import Decimal

@login_required
def booking_confirm(request):
    booking_data = request.session.get('booking_data')
    if not booking_data:
        messages.error(request, 'No booking data found.')
        return redirect('home')
    
    showtime = get_object_or_404(ShowTime, id=booking_data['showtime_id'])
    seats = Seat.objects.filter(id__in=booking_data['selected_seats'])
    
    return render(request, 'bookings/booking_confirm.html', {
        'showtime': showtime,
        'seats': seats,
        'total_amount': booking_data['total_amount']
    })

@login_required
def process_payment(request):
    if request.method == 'POST':
        booking_data = request.session.get('booking_data')
        if not booking_data:
            messages.error(request, 'No booking data found.')
            return redirect('home')
        
        payment_method = request.POST.get('payment_method')
        showtime = get_object_or_404(ShowTime, id=booking_data['showtime_id'])
        
        # Create booking
        booking = Booking.objects.create(
            user=request.user,
            showtime=showtime,
            total_amount=Decimal(booking_data['total_amount']),
            payment_status='completed'
        )
        
        # Create booked seats
        for seat_id in booking_data['selected_seats']:
            seat = get_object_or_404(Seat, id=seat_id)
            BookedSeat.objects.create(booking=booking, seat=seat)
        
        # Create payment record
        Payment.objects.create(
            booking=booking,
            payment_method=payment_method,
            transaction_id=str(uuid.uuid4())[:10],
            amount=Decimal(booking_data['total_amount'])
        )
        
        # Clear session data
        del request.session['booking_data']
        
        messages.success(request, 'Payment successful! Your tickets have been booked.')
        return redirect('ticket_view', booking_id=booking.booking_id)
    
    return render(request, 'bookings/payment.html')

@login_required
def ticket_view(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    booked_seats = BookedSeat.objects.filter(booking=booking)
    
    return render(request, 'bookings/ticket.html', {
        'booking': booking,
        'booked_seats': booked_seats
    })

@login_required
def download_ticket(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    booked_seats = BookedSeat.objects.filter(booking=booking)
    
    template = get_template('bookings/ticket_pdf.html')
    html = template.render({
        'booking': booking,
        'booked_seats': booked_seats
    })
    
    # Create response with proper headers for download
    response = HttpResponse(html, content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename="MovieTix_Ticket_{booking_id}.html"'
    
    return response