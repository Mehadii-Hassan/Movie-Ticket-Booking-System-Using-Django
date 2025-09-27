from django.contrib import admin
from .models import Movie, Theater, ShowTime, Seat

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'duration', 'release_date', 'is_active']
    list_filter = ['genre', 'is_active', 'release_date']
    search_fields = ['title', 'genre']
    list_editable = ['is_active']

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'total_seats']
    search_fields = ['name', 'location']

@admin.register(ShowTime)
class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ['movie', 'theater', 'show_date', 'show_time', 'price']
    list_filter = ['show_date', 'theater']
    search_fields = ['movie__title', 'theater__name']

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['theater', 'row', 'number', 'seat_type']
    list_filter = ['theater', 'seat_type']
    search_fields = ['theater__name']