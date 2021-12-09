from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    total_borrow_count = models.IntegerField(default=0)
    borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="borrowed_by")
    date_borrowed = models.DateTimeField(auto_now_add = True)
    date_added = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    review = models.TextField(null=True)
    stars = models.IntegerField(default = 3,
    validators=[MinValueValidator(0), MaxValueValidator(5)])
    date_added = models.DateTimeField(auto_now_add = True, null=True)
    date_modified = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return f'{self.board_game}, {self.review[:50]}'