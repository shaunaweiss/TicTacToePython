from .models import Board, Space
from game.forms import BoardForm
import json
from datetime import datetime
from game.controller import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

"""Game view"""
def index(request):
    board_id = None
    if request.session.get('board_id') == None:
        return HttpResponseRedirect('/create-game-redirect')
    else:
        board_id = request.session.get('board_id')
    board_form = BoardForm()
    game = play_game(board_id)
    json_game = json.dumps(game)
    return render(request, 'game/detail.html', {'board_form': board_form, 'game': json_game})

"""Method that communicates with the controller to update the view"""
def move_redirect(request):
    if request.method == "POST":
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board_id = board_form.cleaned_data['board']
            space_id = board_form.cleaned_data['square']
            space_value = board_form.cleaned_data['turn']
            update_board(board_id, space_id, space_value)
            return HttpResponseRedirect('/')
        else:
            board_form = BoardForm()
    return HttpResponseRedirect('/')

"""Creates a game board"""
def create_game_redirect(request):
    board_id = create_board_and_spaces()
    request.session['board_id'] = board_id
    return HttpResponseRedirect('/')
