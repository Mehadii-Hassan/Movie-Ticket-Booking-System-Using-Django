from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Movie, ShowTime, Theater, Seat
from bookings.models import BookedSeat, Booking
from datetime import date

def home(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'home.html', {'movies': movies})

def movie_list(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    showtimes = ShowTime.objects.filter(movie=movie, show_date__gte=date.today())
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'showtimes': showtimes
    })

@login_required
def seat_selection(request, showtime_id):
    showtime = get_object_or_404(ShowTime, id=showtime_id)
    theater = showtime.theater
    
    # Get all seats for this theater
    seats = Seat.objects.filter(theater=theater).order_by('row', 'number')
    
    # Get already booked seats for this showtime
    booked_seats = BookedSeat.objects.filter(
        booking__showtime=showtime,
        booking__payment_status='completed'
    ).values_list('seat_id', flat=True)
    
    # Organize seats by rows
    seat_rows = {}
    for seat in seats:
        if seat.row not in seat_rows:
            seat_rows[seat.row] = []
        seat_rows[seat.row].append({
            'seat': seat,
            'is_booked': seat.id in booked_seats
        })
    
    return render(request, 'movies/seat_selection.html', {
        'showtime': showtime,
        'seat_rows': seat_rows,
        'theater': theater
    })

@login_required
def book_seats(request, showtime_id):
    if request.method == 'POST':
        showtime = get_object_or_404(ShowTime, id=showtime_id)
        selected_seats = request.POST.getlist('seats')
        
        if not selected_seats:
            messages.error(request, 'Please select at least one seat.')
            return redirect('seat_selection', showtime_id=showtime_id)
        
        # Calculate total amount
        total_amount = len(selected_seats) * showtime.price
        
        # Store booking data in session
        request.session['booking_data'] = {
            'showtime_id': showtime_id,
            'selected_seats': selected_seats,
            'total_amount': str(total_amount)
        }
        
        return redirect('booking_confirm')
    
    return redirect('seat_selection', showtime_id=showtime_id)