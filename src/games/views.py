from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BoardGame, Review
from .forms import BoardGameForm, ReviewForm

# Create your views here.
def index(request):
    return render(request, 'games/index.html')

@login_required
def board_games(request):
    board_games = BoardGame.objects.order_by('date_added')
    context = {'board_games' : board_games}
    return render(request, 'games/board_games.html', context)

@login_required
def board_game(request, boardgame_id):
    board_game = BoardGame.objects.get(id=boardgame_id)
    reviews = board_game.review_set.order_by('-date_added')
    context = {'board_game': board_game, 'reviews': reviews}
    return render(request, 'games/board_game.html', context)

@login_required
def new_board_game(request):
    """Add a new board game."""
    if request.method != 'POST':
        form = BoardGameForm()
    else:
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            new_board_game = form.save(commit=False)
            new_board_game.owner = request.user
            new_board_game.borrowed_by = request.user
            form.save()
            return redirect('games:board_games')
    
    context = {'form': form}
    return render(request, 'games/new_board_game.html', context)

@login_required
def new_review(request, boardgame_id):
    boardgame = BoardGame.objects.get(id=boardgame_id)
    
    if request.method != "POST":
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.owner = request.user
            new_review.board_game = boardgame
            new_review.save()
            return redirect("games:board_game", boardgame_id=boardgame_id)

    context = {"boardgame": boardgame, "form": form}
    return render(request, "games/new_review.html", context)

def edit_review(request, review_id):
    review = Review.objects.get(id=review_id)
    board_game = review.board_game

    if request.method != "POST":
        form = ReviewForm(instance=review)
    else:
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("games:board_game", boardgame_id=board_game.id)
    context = {"review": review, "board_game": board_game, "form": form}
    return render(request, "games/edit_review.html", context)

def edit_board_game(request, boardgame_id):
    board_game = BoardGame.objects.get(id=boardgame_id)

    if request.method != "POST":
        form = BoardGameForm(instance=board_game)
    else:
        form = BoardGameForm(instance=board_game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("games:board_games")
    context = {"board_game": board_game, "form": form}
    return render(request, "games/edit_board_game.html", context)

def delete_board_game(request, boardgame_id):
    board_game = BoardGame.objects.get(id=boardgame_id)
    reviews = board_game.review_set.all()
    board_game.delete()
    reviews.delete()
    return redirect("games:board_games")

def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return redirect("games:board_games")

def borrow(request, boardgame_id):
    obj = BoardGame.objects.get(id=boardgame_id)
    obj.borrowed = True
    obj.borrowed_by = request.user
    obj.total_borrow_count = obj.total_borrow_count + 1
    obj.save()
    return redirect("games:board_games")

def returns(request, boardgame_id):
    obj = BoardGame.objects.get(id=boardgame_id)
    obj.borrowed = False
    obj.borrowed_by = request.user
    obj.save()
    return redirect("games:board_games")

