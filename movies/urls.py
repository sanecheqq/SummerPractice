from django.urls import path, include

from . import views
from .views import index_page, loginPage, logoutUser, player_page, landing_page, all_filter, search_movies, registerPage

urlpatterns = [
    path('', landing_page),
    path('base/', index_page),
    

    path('<str:category>', all_filter),

    path('search_movies/', views.search_movies, name='search_movies'),
    path('movie/<int:kinopoisk_id>', player_page),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('base/', views.home, name="home")
]