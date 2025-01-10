from django.urls import path 

from . import views

# creating variable for UrlPatterns 
urlpatterns = [
    # 'index' view url path
    path("", views.index, name="index"),
    path("movies", views.movies, name="movies"),
    path("tvshows", views.tvshows, name="tvshows"),
    path("kids", views.kids, name="kids"),
    path("mylist", views.mylist, name="mylist"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup")
]