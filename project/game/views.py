from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import game
from .models import Board, Space
from game.forms import BoardForm, PartialBoardForm, BoardFormSet
from django.forms import modelformset_factory


def index(request):    
    # board_form = BoardForm()
    # return render(request, 'game/index.html', {'board_form':board_form})
    board_list = Board.objects.order_by('-pub_date')[:]
    context = {
        'board_list': board_list
    }
    # output= ', '.join([b.game_name for b in board_list])
    return render(request, 'game/index.html', context)
    # return HttpResponse(output)

def detail(request, board_id):
        # board_form = BoardForm()

    # board = get_object_or_404(Board, pk=board_id)
    # return render(request, 'game/detail.html', {'board': board})

    formset = BoardFormSet(queryset=Space.objects.filter(board_space=board_id))
    if request.method == 'POST':
        formset = BoardFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = BoardFormSet()

    return render(request, 'game/detail.html', {'formset': formset})

    # BoardFormSet = modelformset_factory(Board, Space, fields=('id', 'board_space', 'space_value'))

    # if request.method == 'POST':
    #     formset = BoardFormSet(request.POST, request.FILES, instance=board)
    #     if formset.is_valid():
    #         formset.save()
    #         # do something.
    # else:
    #     formset = BoardFormSet()

    # context = {
    #     'formset': formset,
    #     'board': board
    # }
    # return render(request, 'game/detail.html', context)

    # if request.method == 'POST':
    #     form = BoardForm(board_id, request.POST)
    #     if form.is_valid():
    #         board = form.save(commit=False)
    #         board.id = board_id
    #         board.save()
    #         return redirect('results')
    # else:
    #     form = BoardForm(board_id)
    # return render(request, 'game/details.html', {'form': form})


def results(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'game/results.html', {'board': board})
    # response = "You're looking at the results of board %s."
    # return HttpResponse(response % board_id)

def move(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    try:
        selected_space = board.space_set.get(pk=request.POST['space'])
    except (KeyError, Space.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'game/detail.html', {
            'board': board,
            'error_message': "You didn't select a space.",
        })
    else:
        # selected_space.votes += 1
        selected_space.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('game:results', args=(board.id,)))

    # return HttpResponse("You're taking a turn on board %s." % board_id)

