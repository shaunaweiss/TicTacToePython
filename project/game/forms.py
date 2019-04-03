from django import forms

class BoardForm(forms.Form):
    square = forms.ChoiceField(choices=(('0', '0'), ('1', '1'), ('2', '2'),
    ('3', '3'), ('4', '4'), ('5', '5'),('6', '6'), ('7', '7'), ('8', '8')))