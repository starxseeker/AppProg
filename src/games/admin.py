from django.contrib import admin

from .models import BoardGame, Review, Genre

admin.site.register(BoardGame)
admin.site.register(Review)
admin.site.register(Genre)
