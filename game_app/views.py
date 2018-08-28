# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def game(request):
    return render(request, 'tac.html')

def addPlayer(request, name):
    print >>sys.stderr, name

# Create your views here.
