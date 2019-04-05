from .models import Board, Space

def update_board(board_id, space_id, space_value):
    try:
        if int(space_id)<=8 and int(space_id)>=0 and isinstance(int(space_id), int):
            board = Board.objects.get(id=board_id)
            space = Space.objects.get(board_space=board_id, space_id=space_id)
            if space.space_value == '-':
                space.space_value = space_value
            space.save()
    except:
        pass

def create_board_and_spaces():
    highest_value = Board.objects.all().order_by('-id')[0].id + 1
    board_object = Board.objects.create(id=highest_value)
    board_object.save()
    for space in range(0,9):
        space_object = Space.objects.create(space_id=space, board_space=board_object, space_value='-')
        space_object.save()
    return highest_value


def play_game(board_id):
    board_state = get_board_from_model(board_id)
    result = determine_winner(board_state)
    turn = get_turn_from_model(board_state)
    return {'board_state': board_state, 'result': result, 'turn': turn, 'board_id':board_id}

def get_board_from_model(board_id):
    board_array = []
    board = Space.objects.filter(board_space=board_id).order_by('space_id')
    for space in board:
        board_array.append(space.space_value)
    return board_array

def get_turn_from_model(board_state):
    value_count = 0
    for space in board_state:
        if space == 'x' or space == 'o':
            value_count += 1
    if value_count % 2 == 0:
        return 'x'
    else:
        return 'o'

def determine_winner(board_state):
    result = check_for_winner(board_state)
    if result != None:
        return result + ' is the winner!'
    else:
        return None

def check_for_winner(board_state):
    if ((board_state[0] == 'x' and board_state[1] == 'x' and board_state[2] == 'x') or
            (board_state[3] == 'x' and board_state[4] == 'x' and board_state[5] == 'x') or
            (board_state[6] == 'x' and board_state[7] == 'x' and board_state[8] == 'x') or
            (board_state[0] == 'x' and board_state[3] == 'x' and board_state[6] == 'x') or
            (board_state[1] == 'x' and board_state[4] == 'x' and board_state[7] == 'x') or
            (board_state[2] == 'x' and board_state[5] == 'x' and board_state[8] == 'x') or
            (board_state[0] == 'x' and board_state[4] == 'x' and board_state[8] == 'x') or
            (board_state[2] == 'x' and board_state[4] == 'x' and board_state[6] == 'x')):
        return 'x'
    elif ((board_state[0] == 'o' and board_state[1] == 'o' and board_state[2] == 'o') or
          (board_state[3] == 'o' and board_state[4] == 'o' and board_state[5] == 'o') or
          (board_state[6] == 'o' and board_state[7] == 'o' and board_state[8] == 'o') or
          (board_state[0] == 'o' and board_state[3] == 'o' and board_state[6] == 'o') or
          (board_state[1] == 'o' and board_state[4] == 'o' and board_state[7] == 'o') or
          (board_state[2] == 'o' and board_state[5] == 'o' and board_state[8] == 'o') or
          (board_state[0] == 'o' and board_state[4] == 'o' and board_state[8] == 'o') or
          (board_state[2] == 'o' and board_state[4] == 'o' and board_state[6] == 'o')):
        return 'o'
    else:
        return None