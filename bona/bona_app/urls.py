from django.urls import path 

from . import views

# creating variable for UrlPatterns 

urlpatterns = [
    
    # 'index' view url path
    path("", views.home, name="home"),
    path("movies", views.movies, name="movies"),
    path("tvshows", views.tvshows, name="tvshows"),
    path("kids", views.kids, name="kids"),
    path("mylist", views.mylist, name="mylist"),
    path("login", views.login_view, name="login_view"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout_view, name="logout_view"),
]