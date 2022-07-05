from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def landing_page(request):
    return render(request, 'landing.html')

def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def player_page(request, kinopoisk_id):
    assert isinstance(kinopoisk_id, object)
    movie = Movie.objects.get(kinopoisk_id=kinopoisk_id)
    return render(request, 'movies/player.html', {'movie': movie})