from django import forms
from django import forms
from django.forms import ModelForm
from .models import Board, Space
from django.forms import modelformset_factory


class BoardForm(ModelForm):
    class Meta:
        model = Space
        fields = '__all__'

class PartialBoardForm(ModelForm):
    class Meta:
        model = Space
        exclude = ['board_space']
    
# class BoardForm (forms.ModelForm):
#     class Meta:
#         model = Space
#         fields= ('id', 'space_value')
    
#     def __init__(self, board_space, *args, **kwargs):
#         super(BoardForm, self).__init__(*args, **kwargs)
#         self.fields['board_space'].queryset = Board.objects.filter(id = board_space)


BoardFormSet = modelformset_factory(Space, fields=('id', 'board_space', 'space_value'))



# class BoardForm(forms.Form):
#     square = forms.ChoiceField(choices=(('0', '0'), ('1', '1'), ('2', '2'),
#     ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8')))