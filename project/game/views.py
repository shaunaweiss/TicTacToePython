from django.http import HttpResponse
# import game


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")

# def get_board(request):
#     board = game.
