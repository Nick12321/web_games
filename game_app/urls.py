from django.urls import path
from . import views

urlpatterns  =[
    path ('tictactoe/', views.game),
    path ('', views.home),
    path ('addPlayer/', views.addPlayer),
    path ('choosePlayer/', views.choosePlayer),
    path ('saveScore/', views.saveScore),
]
