from django.core.management.base import BaseCommand, CommandError
from game.models import *
from game.controller import *
import unittest

class TestController(unittest.TestCase):

    def test_play_game(self):
        sample_board = ['x', 'o', '-', 'x', 'o', '-', 'x', 'o', '-']
        board_id = Board.objects.all().order_by('-id')[0].id + 1
        board = Board.objects.create(id=board_id)
        board.save()
        for space in range(0, 9):
            space_object = Space.objects.create(space_id=space, board_space=board, space_value=sample_board[space])
            space_object.save()
        self.assertEquals(play_game(board_id), {'board_state':sample_board, 'result':'x is the winner!', 'turn':'x', 'board_id':board_id})
        Board.objects.get(id=board_id).delete()

    def test_create_board_and_spaces(self):
        board_id = create_board_and_spaces()
        self.assertTrue(Board.objects.filter(id=board_id).exists())
        Board.objects.get(id=board_id).delete()

    def test_update_board(self):
        new_value = 'o'
        sample_board = ['x', 'o', '-', 'x', 'o', '-', 'x', 'o', '-']
        board_id = Board.objects.all().order_by('-id')[0].id + 1
        board = Board.objects.create(id=board_id)
        board.save()
        for space in range(0, 9):
            space_object = Space.objects.create(space_id=space, board_space=board, space_value=sample_board[space])
            space_object.save()
        """Value before updating"""
        self.assertEquals(Space.objects.get(space_id=2, board_space=board).space_value, '-')
        update_board(board_id, 2, new_value)
        """Value after updating"""
        self.assertEquals(Space.objects.get(space_id=2, board_space=board).space_value, 'o')
        update_board(board_id, 2, new_value)
        """Fails to update because value already exists in the space"""
        self.assertFalse(Space.objects.get(space_id=2, board_space=board).space_value=='x')


    def test_get_board_from_model(self):
        sample_board = ['x', 'o', '-', 'x', 'o', '-', 'x', 'o', '-']
        board_id = Board.objects.all().order_by('-id')[0].id + 1
        board = Board.objects.create(id=board_id)
        board.save()
        for space in range(0, 9):
            space_object = Space.objects.create(space_id=space, board_space=board, space_value=sample_board[space])
            space_object.save()
        self.assertEqual(get_board_from_model(board_id), sample_board)
        Board.objects.get(id=board_id).delete()

    def test_get_turn_from_model(self):
        board_state_1 = ['x', 'o', 'x', '-', '-', '-', '-', '-', '-', ]
        board_state_2 = ['x', 'o', 'x', 'o', '-', '-', '-', '-', '-', ]
        self.assertEqual(get_turn_from_model(board_state_1), 'o')
        self.assertEqual(get_turn_from_model(board_state_2), 'x')

    def test_check_for_winner(self):
        board_state_1 = ['x', 'x', 'x', '-', '-', '-', '-', '-', '-', ]
        board_state_2 = ['-', '-', '-', '-', '-', '-', '-', '-', '-', ]
        board_state_3 = ['o', 'o', 'o', '-', '-', '-', '-', '-', '-', ]
        board_state_4 = ['x', '-', '-', '-', 'x', '-', '-', '-', 'x', ]
        board_state_5 = ['-', '-', 'o', '-', 'o', '-', 'o', '-', '-', ]
        board_state_6 = ['x', '-', '-', 'x', '-', '-', 'x', '-', '-', ]
        board_state_7 = ['-', 'o', '-', '-', 'o', '-', '-', 'o', '-', ]
        board_state_8 = ['-', '-', 'x', '-', '-', 'x', '-', '-', 'x', ]
        board_state_9 = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x', ]
        self.assertEqual(check_for_winner(board_state_1), 'x')
        self.assertEqual(check_for_winner(board_state_2), None)
        self.assertEqual(check_for_winner(board_state_3), 'o')
        self.assertEqual(check_for_winner(board_state_4), 'x')
        self.assertEqual(check_for_winner(board_state_5), 'o')
        self.assertEqual(check_for_winner(board_state_6), 'x')
        self.assertEqual(check_for_winner(board_state_7), 'o')
        self.assertEqual(check_for_winner(board_state_8), 'x')
        self.assertEqual(check_for_winner(board_state_9), 'x')

    def test_determine_winner(self):
        board_state_1 = ['x', 'x', 'x', '-', '-', '-', '-', '-', '-', ]
        board_state_2 = ['o', 'o', 'o', '-', '-', '-', '-', '-', '-', ]
        board_state_3 = ['-', '-', '-', '-', '-', '-', '-', '-', '-', ]
        self.assertEqual(determine_winner(board_state_1), 'x is the winner!')
        self.assertEqual(determine_winner(board_state_2), 'o is the winner!')
        self.assertEqual(determine_winner(board_state_3), None)

"""Allows the tests to be run from command line"""
class Command(BaseCommand):
    def handle(self, *args, **options):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestController)
        unittest.TextTestRunner().run(suite)