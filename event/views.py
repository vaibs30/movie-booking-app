import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.models import Group
from django.utils.dateparse import parse_datetime

from .models import User, Movie, Screen


def index(request):
    movies = Movie.objects.all()
    return render(request, 'event/index.html', {'movies' : movies})

@csrf_exempt
@login_required
def movie(request, id):
    movie_obj = Movie.objects.get(id = id)
    screen_obj = Screen.objects.filter(movie = id)
    return render(request, 'event/movie.html', {'movie': movie_obj, 'screens': screen_obj})

@csrf_exempt
@login_required
def book(request):
    if request.method == "POST":
        print("creating...")
        data = json.loads(request.body)
        print(data)
        screen = data.get("screen", "")
        movie_id = data.get("movie_id", "")
        row = data.get("row", "")
        movie = Movie.objects.get(id = movie_id)
        screen_obj = Screen.objects.get(movie = movie, name = screen)
        print(screen_obj.A)
        if row == "A":
            screen_obj.A -= 1
        elif row == "B":
            screen_obj.B -= 1
        elif row == "C":
            screen_obj.C -= 1
        elif row == "D":
            screen_obj.D -= 1
        screen_obj.save()
        return JsonResponse({"message" : "Movie has been created successfully"})
    else:
        return render(request, 'event/movie.html')


@csrf_exempt
@login_required
def create(request):
    if request.method == "POST":
        print("creating...")
        #Receiving the values

        data = json.loads(request.body)
        title = data.get("title", "")
        description = data.get("description", "")
        rating = data.get("rating", "")
        cast = data.get("cast", "")
        imageURL = data.get("imageURL", "")
        royal = data.get("royal", "")
        elite = data.get("elite", "")
        economy = data.get("economy", "")
        upcoming = data.get("upcoming", "")
        
        screen_list = []
         
        if royal == True:
            screen_list.append("Royal")

        if elite == True:
            screen_list.append("Elite")
        
        if economy == True:
            screen_list.append("Economy")

        movie_obj = Movie(name = title, description = description, rating = rating, cast = cast, imageURL = imageURL,
        is_upcoming = upcoming
         )
        movie_obj.save()
        for screen in screen_list:
            screen_obj = Screen(movie = movie_obj, name = screen, A=10, B=10, C=10, D=10 )
            screen_obj.save()
        return JsonResponse({"message" : "Movie has been created successfully"})
    
    else:
        return render(request, 'event/create.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "event/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "event/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "event/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "mail/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "event/register.html")
