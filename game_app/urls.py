from django.urls import path
from . import views

urlpatterns  =[
    path ('tictactoe/', views.game),
    path ('', views.home),
    path('<char:name>/', views.addPlayer )
]
