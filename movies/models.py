from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    total_seats = models.IntegerField(default=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)
    duration = models.IntegerField(help_text="Duration in minutes")
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    show_date = models.DateField()
    show_time = models.TimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        unique_together = ('movie', 'theater', 'show_date', 'show_time')
    
    def __str__(self):
        return f"{self.movie.title} - {self.theater.name} - {self.show_date} {self.show_time}"

class Seat(models.Model):
    SEAT_TYPES = [
        ('regular', 'Regular'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ]
    
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    row = models.CharField(max_length=2)
    number = models.IntegerField()
    seat_type = models.CharField(max_length=10, choices=SEAT_TYPES, default='regular')
    
    class Meta:
        unique_together = ('theater', 'row', 'number')
    
    def __str__(self):
        return f"{self.row}{self.number}"