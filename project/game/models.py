from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField('date started')
    game_name = models.CharField(max_length=200, default=None)

    def _str_(self):
        return self.game_name

class Space(models.Model):

    VALUES = (
        (0, 'X'), (1, 'O')
    )
    id = models.PositiveIntegerField(primary_key=True, validators=[MinValueValidator(0), MaxValueValidator(8)])
    board_space = models.ForeignKey(Board, on_delete=models.CASCADE)
    space_value = models.IntegerField(choices=VALUES, default=None)
    
    def _str_(self):
        return ' '.join(self.board_space, self.spacee_value)



