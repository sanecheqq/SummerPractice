from django.urls import path, include

from . import views
from .views import index_page, player_page, landing_page, all_filter

urlpatterns = [
    path('', landing_page),
    path('base/', index_page),

    path('<str:category>', all_filter),

    path('search_movies/', views.search_movies, name='search_movies'),
    path('movie/<int:kinopoisk_id>', player_page),
]