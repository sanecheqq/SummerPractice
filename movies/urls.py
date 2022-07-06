from django.urls import path, include
from .views import index_page, player_page, landing_page

urlpatterns = [
    path('', landing_page),
    path('base.html/', index_page),
    path('movie/<int:kinopoisk_id>', player_page),
]