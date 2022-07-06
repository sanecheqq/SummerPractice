from django.urls import path, include

from . import views
from .views import index_page, player_page, landing_page

urlpatterns = [
    path('', landing_page),
    path('base.html/', index_page),
    path('search_movies/', views.search_movies, name='search_movies'),
    path('movie/<int:kinopoisk_id>', player_page),
]