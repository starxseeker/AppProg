from django import forms

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
        labels = {"review": "Review", "stars": "Stars"}

SORT_CHOICES= [
    ('name', 'name'),
    ('genre', 'genre'),
    ('-total_borrow_count', 'borrow count'),
    ('borrowed', 'availability'),
    ]

class SortForm(forms.Form):
    sort = forms.CharField(label='Sort by', widget=forms.Select(choices=SORT_CHOICES), initial="name")