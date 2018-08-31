from django import forms
from .models import Player

class addPlayerForm(forms.Form):
    name = forms.CharField(help_text="Enter your name.", max_length = 300)

class choosePlayerForm(forms.Form):
    Players = Player.objects.all()

    nameOfPlayers = []

    for player in Players:
        nameOfPlayers.append((player.pk, player.name))

    player1 = forms.ChoiceField(choices = nameOfPlayers)
    player2 = forms.ChoiceField(choices = nameOfPlayers)