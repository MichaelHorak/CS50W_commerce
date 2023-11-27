from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index_view, name="index"),
    # path("login", LoginView.as_view(template_name="auctions/login.html"), name="login"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("categories", views.categories_view, name="categories"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("create listing", views.create_listing_view, name="create listing"),
    path("closed listings", views.closed_listings_view, name="closed listings")
]
