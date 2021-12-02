"""Defines URL patterns for games."""

from django.urls import path
from . import views

app_name = "games"
urlpatterns = [
    # Home page
    path("", views.index, name="index")
]