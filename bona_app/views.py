from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import User
from django.db import IntegrityError
from django.http import Http404
from bona_app.models import User, Movie

# Create your views here.

# creating index view
def home(request):
    # MAIN MOVIE OBJECT GETTER
    main_movie = Movie.objects.get(pk=16)
    todays_picks = Movie.objects.all()[1:8]
    trending = Movie.objects.all()[1:8]
    new_movie = Movie.objects.all()[1:8]
    top_searches = Movie.objects.all()[1:8]
    my_list = Movie.objects.all()[1:8]

    # RENDERING HOME.HTML TEMPLATE WITH 'main_movie' VARIABLE
    return render(request, "bona_templates/home.html", {
        "main_movie": main_movie,
        "todays_picks": todays_picks,
        "trending": trending,
        "new_movie": new_movie,
        "top_searches": top_searches,
        "my_list": my_list
        })

def movies(request):
    # MAIN MOVIE OBJECT GETTER
    main_movie = Movie.objects.get(pk=16)
    trending = Movie.objects.all()[1:8]
    top_movie_picks = Movie.objects.all()[1:8]
    critically_acclaimed = Movie.objects.all()[1:8]
    award_winning = Movie.objects.all()[1:8]
    my_list = Movie.objects.all()[1:8]
    
    # RENDERING MOVIES.HTML TEMPLATE WITH 'main_movie' VARIABLE
    return render(request, "bona_templates/movies.html", {
        "main_movie": main_movie,
        "trending": trending,
        "top_movie_picks": top_movie_picks,
        "critically_acclaimed": critically_acclaimed,
        "award_winning": award_winning,
        "my_list": my_list
        })

def tvshows(request):
    # MAIN MOVIE OBJECT GETTER
    main_movie = Movie.objects.get(pk=16)
    trending = Movie.objects.all()[8:15]
    award_winning = Movie.objects.all()[8:15]
    top_tv_shows = Movie.objects.all()[8:15]
    critically_acclaimed = Movie.objects.all()[8:15]
    my_list = Movie.objects.all()[8:15]

    # RENDERING TVSHOWS.HTML TEMPLATE WITH 'main_movie' VARIABLE
    return render(request, "bona_templates/tvshows.html", {
        "main_movie": main_movie,
        "trending": trending,
        "award_winning": award_winning,
        "top_tv_shows": top_tv_shows,
        "critically_acclaimed": critically_acclaimed,
        "my_list": my_list
    })

def kids(request):
    # MAIN MOVIE OBJECT GETTER
    main_movie = Movie.objects.get(pk=16)

    # RENDERING KIDS.HTML TEMPLATE WITH 'main_movie' VARIABLE
    return render(request, "bona_templates/kids.html", {"main_movie": main_movie})

def mylist(request):

    my_list = Movie.objects.all()[1:]
    # return Httpresponse in mylist view
    return render(request, "bona_templates/mylist.html", {
        "my_list": my_list
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if fields are filled properly
        if username == '' and password == '':
            return render(request, "bona_templates/login.html", {
                "username_password_message": "Enter Username and Password.",
            })
        elif username == '' or password == '':
            return render(request, "bona_templates/login.html", {
                "username_message": "You Forgot To Enter Username Or Password.",
            })
        
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "bona_templates/login.html", {
                "message": "Invalid Username and/or Password."
            })

    else:
        return render(request, "bona_templates/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["password_confirm"]

        # Check if fields are filled properly
        if username == '' and password == '' and confirmation == '':
            return render(request, "bona_templates/signup.html", {
                "error_message1": "Fill All Fields",
            })
        if username == '':
            return render(request, "bona_templates/signup.html", {
                "username_error_message": "You Forgot To Enter Username.",
            })
        if email == '':
            return render(request, "bona_templates/signup.html", {
                "email_error_message": "You Forgot To Enter Email.",
            })
        if password == '':
            return render(request, "bona_templates/signup.html", {
                "password_error_message": "You Forgot To Enter Password.",
            })
        if confirmation == '':
            return render(request, "bona_templates/signup.html", {
                "confirmation_error_message": "You Forgot To Enter Confirmation.",
            })
        if password != confirmation:
            return render(request, "bona_templates/signup.html", {
                "password_message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "bona_templates/signup.html", {
                "user_message": "User already exists."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "bona_templates/signup.html")