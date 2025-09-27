from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('seat-selection/<int:showtime_id>/', views.seat_selection, name='seat_selection'),
    path('book-seats/<int:showtime_id>/', views.book_seats, name='book_seats'),
]