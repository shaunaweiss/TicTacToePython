from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class Board(models.Model):
    id = models.AutoField(primary_key=True)

class Space(models.Model):

    VALUES = (
        ('x', 'x'), ('o', 'o'), ('-', '-')
    )
    space_id = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(8)])
    board_space = models.ForeignKey(Board, on_delete=models.CASCADE)
    space_value = models.CharField(choices=VALUES, default='-', max_length=1)