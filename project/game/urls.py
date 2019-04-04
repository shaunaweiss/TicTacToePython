from django.urls import path

from . import views

app_name = 'game' 

urlpatterns = [

    path('', views.index, name='index'),

    # ex: /game/1
    path('<int:board_id>/', views.detail, name='detail'),

    #ex: /game/1/results/
    path('<int:board_id>/results/', views.results, name='results'),

    #ex: /game/1/move/
    path('<int:board_id>/move/', views.move, name='move')
]