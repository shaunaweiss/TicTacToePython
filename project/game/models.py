from _ast import Tuple
from django.db import models

# Create your models here.

#
# class Board(models.Model):
#     # spaces_available = models.CharField(("Spaces"), max_length=50)
#
#     # question_text = models.CharField(max_length=200)
#     # pub_date = models.DateTimeField('date published'
#     # board = Square()
#     game_board = models.CharField(max_length=8, default=''*8)
#
#     winning_cases = (
#         # Rows
#         (0, 1, 2),
#         (3, 4, 5),
#         (6, 7, 8),
#         # Cols
#         (0, 3, 6),
#         (1, 4, 7),
#         (2, 5, 8),
#         #Diagnols
#         (6, 4, 0),
#         (8, 4, 0),
#     )
#     #
#     # winning_values = (
#     #     'XXX', 'OOO'
#     # )
#
#     # def stringify_board(self):
#     #
#     #
#
#     @property
#     def board_state(self):
#         return 'Winning';
#
#
#
#
# class Space(models.Model):
#     # space_selected = models.models.ForeignKey(Board, verbose_name=_(""), on_delete=models.CASCADE)
#     space_selected = models.IntegerField(default=None)
#
#     SQUARE_VALUES = (
#         ('X', True), ('O', False)
#     )
#
#     value = models.CharField(max_length=1, choices=SQUARE_VALUES)

class Board(models.Model):
    id = models.IntegerField(primary_key=True)


class Space(models.Model):

    VALUES = (
        (0, 'X'), (1, 'O')
    )
    id = models.IntegerField(primary_key=True)
    board_space = models.ForeignKey(Board, on_delete=models.CASCADE)
    space_value = models.IntegerField(choices=VALUES, default=None)



