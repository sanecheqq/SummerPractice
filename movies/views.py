from curses.ascii import CR
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm

from .models import Movie
from .forms import CreateUserForm


def landing_page(request):
    return render(request, 'landing.html')


def index_page(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})


def player_page(request, kinopoisk_id):
    assert isinstance(kinopoisk_id, object)
    movie = Movie.objects.get(kinopoisk_id=kinopoisk_id)
    return render(request, 'movies/player.html', {'movie': movie})


def search_movies(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Movie.objects.filter(name__contains=searched)

        return render(request,
                      'movies/search_movies.html',
                      {'searched': searched,
                       'venues': venues})
    else:
        return render(request,
                      'movies/search_movies.html',
                      {})

def all_filter(request, category):
   movies = Movie.objects.filter(category = category)
   return render(request, 'movies/movie_list.html', {'movies': movies})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)