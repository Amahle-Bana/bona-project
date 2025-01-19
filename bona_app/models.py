from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# ABSTRACTUSER CLASS
class User(AbstractUser):
    pass

# MOVIE CLASS
class Movie(models.Model):

    # AGE RESTRICTIONS DICTIONARY
    AGE_RESTRICTIONS = {
        "E": "Everyone",
        "PG": "Parental Guidance",
        "PG13+": "Parental Guidance 13+",
        "18+": "Adults 18+"
    }
    
    # GENRE DICTIONARY
    GENRE = {
        "Action": "Action",
        "Anime": "Award-Warning",
        "Award-Winning": "Award-Wanning",
        "Classics": "Classics",
        "Comedy": "Comedy",
        "Crime": "Crime",
        "Documentaries": "Documentaries",
        "Dramas": "Dramas",
        "Fantasy": "Fantasy",
        "Horror": "Horror",
        "Kids": "Kids",
        "Family": "Family",
        "Musicals": "Musicals",
        "Romance": "Romance",
        "Sci-Fi": "Sci-Fi",
        "Sports": "Sports",
        "Stand-Up": "Stand-Up",
        "Thriller": "Thriller"
    }

    # MODEL VARIABLES
    movie_name = models.CharField(max_length=50, blank=False, null=True)
    movie_description = models.TextField(max_length=200,blank=False, null=False)
    movie_age_restriction = models.CharField(max_length=30, choices=AGE_RESTRICTIONS, default="E")
    movie_genre = models.CharField(max_length=30, choices=GENRE, default="Action")
    movie_poster = models.ImageField(upload_to='bona_app/static/movies/posters', null=True)
    movie_logo = models.ImageField(upload_to='bona_app/static/movies/logos', null=True)
    movie_trailer = models.FileField(upload_to='bona_app/static/movies/trailers', null=True)

    # DATABASE STRING REPRESENTATION
    def __str__(self):
        return self.movie_name