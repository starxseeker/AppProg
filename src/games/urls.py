"""Defines URL patterns for games."""

from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # A page that shows all board games.
    path('board_games/', views.board_games, name='board_games'),

    # A detail page for a single board game.
    path('board_games/<int:boardgame_id>/', views.board_game, name='board_game'),

    # A page for adding a new board game.
    path('new_board_game/', views.new_board_game, name='new_board_game'),

    # A page for adding a new review.
    path('new_review/<int:boardgame_id>/', views.new_review, name='new_review'),

    # A page for editing reviews.
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),

    # A page for editing board games.
    path('edit_board_game/<int:boardgame_id>/', views.edit_board_game, name='edit_board_game'),

    # A page for deleting board games.
    path('delete_board_game/<int:boardgame_id>/', views.delete_board_game, name='delete_board_game'),

    # A page for deleting reviews.
    path('delete_review/<int:review_id>/', views.delete_review, name="delete_review"),

    # URL to borrow board games.
    path('borrow/<int:boardgame_id>/', views.borrow, name="borrow"),

    # URL to return board games.
    path('returns/<int:boardgame_id>/', views.returns, name="returns"),
]