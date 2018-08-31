# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import addPlayerForm, choosePlayerForm
from .models import Player

player1Name = ""
player2Name = ""

def home(request):
    error = ''
    return render(request, 'home.html', {'error': error})

def game(request):
    return render(request, 'tac.html', {'player1': player1Name, 'player2': player2Name})

def saveScore(request):
    player1Name = request.POST.get("player1")
    player1Name = request.POST.get("player1")
    return render(request, 'tac.html', {'player1': player1Name, 'player2': player2Name})

def choosePlayer(request):
    chooseplayerform = choosePlayerForm()
    if request.method == 'POST':
        answeredForm = choosePlayerForm(request.POST)
        if answeredForm.is_valid():
            player1ID = answeredForm.cleaned_data['player1']
            player2ID = answeredForm.cleaned_data['player2']

            if player1ID == player2ID:
                error = 'You need to choose 2 different players'
                return render(request, 'choosePlayer.html', {'form': chooseplayerform, 'error': error})
            else:
                player1Name = Player.objects.get(pk=player1ID).name
                player2Name = Player.objects.get(pk=player2ID).name

                return render(request, 'tac.html', {'player1': player1Name, 'player2': player2Name})

    elif request.method == 'GET':
        Players = Player.objects.all()
        numberOfPlayers = len(Players)
        if numberOfPlayers > 1:
            error = ''
            return render(request, 'choosePlayer.html', {'form': chooseplayerform, 'error': error})
        else:
            error = "You ned 2 or more players in the database to start playing."
            return render(request, 'home.html', {'error': error}) 

def addPlayer(request):
    addplayerform = addPlayerForm()
    if request.method == 'POST':
        answeredForm = addPlayerForm(request.POST)
        if answeredForm.is_valid():
            userName = answeredForm.cleaned_data['name']

            Players = Player.objects.all()

            nameOfPlayers = []

            for player in Players:
                nameOfPlayers.append(player.name)

            if userName.upper() in (playerName.upper() for playerName in nameOfPlayers):
                error = 'Name is already taken'
            else:
               newPlayer = Player.objects.create(name = userName)
               error = 'Added a new player: ' + userName 
            

            return render(request, 'addPlayer.html', {'form': addplayerform, 'error': error})

    elif request.method == 'GET':
        error = ''
        return render(request, 'addPlayer.html', {'form': addplayerform, 'error': error})

# Create your views here.
