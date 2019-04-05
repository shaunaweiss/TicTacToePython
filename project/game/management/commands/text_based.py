from django.core.management.base import BaseCommand, CommandError
from game.models import *
from game.controller import *


def display_text_board(board_id):
    board_state = get_board_from_model(board_id)
    return ("\n" + "-------\n|" + board_state[0] + "|" + board_state[1] + "|" + board_state[2] + "|\n" +
            "-------\n|" + board_state[3] + "|" + board_state[4] + "|" + board_state[5] + "|\n" +
            "-------\n|" + board_state[6] + "|" + board_state[7] + "|" + board_state[8] + "|\n-------")


def run():
    board_id = create_board_and_spaces()
    game_running = True
    while game_running == True:
        game_state = play_game(board_id)
        print(display_text_board(board_id))
        if(game_state['result'] != None):
            print(game_state['result'])
            break
        print(game_state['turn'] + "'s turn")
        print("Choose what tile to play (0-8)")
        space_id = input()
        update_board(board_id, space_id, game_state['turn'])


class Command(BaseCommand):
    def handle(self, *args, **options):
        run()