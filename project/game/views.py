from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import game
from game.forms import BoardForm


def index(request):
    board_form = BoardForm()
    return render(request, 'game/index.html', {'board_form':board_form})

# def get_board(request):
#     board = game.
