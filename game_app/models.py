# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=300, unique=True)

class Results(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2')
    score = models.IntegerField(default = 0)
