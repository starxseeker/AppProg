from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class BoardGame(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre, related_name="genres")
    total_borrow_count = 0
    date_borrowed = models.DateTimeField(auto_now_add = True)
    date_added = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.name}, {self.total_borrow_count}'

class Review(models.Model):
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.board_game}, {self.review[:50]}'