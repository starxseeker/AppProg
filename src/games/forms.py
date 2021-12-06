from django import forms
from django.db.models import fields
from django.forms.models import ModelMultipleChoiceField

from .models import BoardGame, Genre, Review

class BoardGameForm(forms.ModelForm):
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())

    class Meta:
        model = BoardGame
        fields = ["name", "genre"]
        labels = {"name": "Board game's name", "genre": "Board game's genre"}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["review", "stars"]
        labels = {"review": "Review", "stars": "Stars(0-5)"}
