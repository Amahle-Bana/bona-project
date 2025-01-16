from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import User
from django.db import IntegrityError


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