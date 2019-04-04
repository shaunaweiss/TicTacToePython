from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import game
from game.forms import BoardForm
from game.models import *
from datetime import *


def index(request):
    # board = Board.objects.create(pub_date=datetime.now(), game_name="yes")
    # board.save()
    # for i in range(8,9):
    #     space = Space.objects.create(id=i, board_space=Board.objects.get(id=1), space_value=1)
    #     space.save()
    if request.method == "POST":
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board = Board.objects.get(id=1)
            space = Space.objects.get(board_space=1, id=board_form.cleaned_data['square'])
            space.save()
            return HttpResponseRedirect('/')
        else:
            board_form = BoardForm()
    board_form = BoardForm()
    return render(request, 'game/index.html', {'board_form':board_form})

