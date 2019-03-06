from django.db import models

# Create your models here.
class Board(models.Model):
    spaces_available = models.CharField(("Spaces"), max_length=50)

    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')


class Move(models.Model):
    # space_selected = models.models.ForeignKey(Board, verbose_name=_(""), on_delete=models.CASCADE)
    space_selected = models.IntegerField(default=None)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)