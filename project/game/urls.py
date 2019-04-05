from django.urls import path

from . import views

app_name = 'game' 

urlpatterns = [

    path('', views.index, name='index'),
    path('move-redirect', views.move_redirect, name='move-redirect'),
    path('create-game-redirect', views.create_game_redirect, name='create-game-redirect'),


]