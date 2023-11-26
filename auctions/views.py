from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms

from .models import User


class NewListingForm(forms.Form):
    listing = forms.CharField(label="New Listing")


def index_view(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)

            # redirect to the next parameter or the index if not present
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")


def categories_view(request):
    return render(request, "auctions/categories.html")


def watchlist_view(request):
    # if no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("auctions:login"))
    return render(request, "auctions/watchlist.html")


def create_listing_view(request):
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = NewListingForm(request.POST)

        # check if form data is valid (server-side)
        if form.is_valid():

            # here insert what to do when the form is valid
            print("Here will be an action about what to do when the form is valid.")
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            # if the form is invalid, re-enter the page with existing information.
            return render(request, "auctions/create_listing.html", {
                "form": form
            })

    # if the user is not authenticated, redirect to login with the next param
    if not request.user.is_authenticated:
        return redirect('auctions:login')

    return render(request, "auctions/create_listing.html", {
        "form": NewListingForm()
    })


def closed_listings_view(request):
    return render(request, "auctions/closed_listings.html")
