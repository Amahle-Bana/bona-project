from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# creating index view
def home(request):
    # return Httpresponse in index view
    return render(request, "bona_templates/home.html")

def movies(request):
    # return Httpresponse in movies view
    return render(request, "bona_templates/movies.html")

def tvshows(request):
    # return Httpresponse in tvshows view
    return render(request, "bona_templates/tvshows.html")

def kids(request):
    # return Httpresponse in kids view
    return render(request, "bona_templates/kids.html")

def mylist(request):
    # return Httpresponse in mylist view
    return render(request, "bona_templates/mylist.html")

def login(request):
    # return Httpresponse in login view
    return render(request, "bona_templates/login.html")

def signup(request):
    # return Httpresponse in signup view
    return render(request, "bona_templates/signup.html")