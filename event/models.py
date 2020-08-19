from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class User(AbstractUser):
    def serialize(self):
        return {
            "username" : self.username,
        }

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    rating = models.IntegerField()
    imageURL = models.URLField(default="https://increasify.com.au/wp-content/uploads/2016/08/default-image.png", blank=False)
    is_upcoming = models.BooleanField(default=False)
    cast = models.CharField(max_length=200)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "price": self.price,
            "imageURL": self.imageURL,
            "description" : self.description,
            "is_showing" : self.is_showing,
            "is_upcoming" : self.is_upcoming,
            "cast": self.cast,
        }

class Screen(models.Model):
    screen_choices = [
        ('Elite', 'Elite'),
        ('Royal', 'Royal'),
        ('Economy', 'Economy'),
    ]
    name = models.CharField(max_length=50, choices= screen_choices)
    A = models.IntegerField(default=10)
    B = models.IntegerField(default=10)
    C = models.IntegerField(default=10)
    D = models.IntegerField(default=10)
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE, related_name="movie")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "D": self.D,
        }



    
