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
    ('name', 'name A-Z'),
    ('-name', 'name Z-A'),
    ('-total_borrow_count', 'borrow count'),
    ('borrowed', 'availability'),
    ]

count = Genre.objects.count()
obj = Genre.objects.all()
for n in range(count):
    test = Genre.objects.get(genre=obj[n])
    SORT_CHOICES.append((test.id, obj[n]))

class SortForm(forms.Form):
    sort = forms.CharField(label='Sort by', widget=forms.Select(choices=SORT_CHOICES), initial="name")