from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# AbstractUser
class User(AbstractUser):
    pass

class Movie(models.Model):
    AGE_RESTRICTIONS = {
        "E": "Everyone",
        "PG": "Parental Guidance",
        "PG 13+": "Parental Guidance 13+",
        "18+": "Adults 18+"
    }
    CATEGORIES = {
        "": "Everyone",
        "PG": "Parental Guidance",
        "PG 13+": "Parental Guidance 13+",
        "18+": "Adults 18+"
    }


    movie_name = models.CharField(max_length=255)
    movie_description = models.TextField(blank=False, null=False)
    movie_age_restriction = models.CharField(max_length=1, choices=AGE_RESTRICTIONS)
    movie_categories = models.ManyToManyField()

    def __str__(self): 
        return self.movie_name
