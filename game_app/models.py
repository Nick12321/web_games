# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=300, unique=True)
    objects = UserManager()

class Results(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2')
    player1wins = models.IntegerField(default = 0)
    player2wins = models.IntegerField(default = 0)
    draws = models.IntegerField(default = 0)
