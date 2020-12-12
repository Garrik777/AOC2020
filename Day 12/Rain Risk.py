from pprint import pprint
from pathlib import Path

def move_in_current_direction(moves, current_direction, x, y):
    if current_direction == "E":
        x = x + moves
    elif current_direction == "W":
        x = x - moves
    elif current_direction == "N":
        y = y + moves
    elif current_direction == "S":
        y = y - moves

    return x,y

def shift_in_current_direction(action, moves, x, y):

    if action == "N":
        y = y + moves
    elif action == "S":
        y = y - moves
    elif action == "E":
        x = x + moves
    elif action == "W":
        x = x - moves

    return x, y

def change_direction(current_direction, action, moves):

    if action == "R":
        if moves == 90:
            if current_direction == "E":
                return "S"
            elif current_direction == "S":
                return "W"
            elif current_direction == "W":
                return "N"
            elif current_direction == "N":
                return "E"

        elif moves == 180:
            if current_direction == "E":
                return "W"
            elif current_direction == "S":
                return "N"
            elif current_direction == "W":
                return "E"
            elif current_direction == "N":
                return "S"

        elif moves == 270:
            if current_direction == "E":
                return "N"
            elif current_direction == "S":
                return "E"
            elif current_direction == "W":
                return "S"
            elif current_direction == "N":
                return "W"
    elif action == "L":
        if moves == 90:
            if current_direction == "E":
                return "N"
            elif current_direction == "S":
                return "E"
            elif current_direction == "W":
                return "S"
            elif current_direction == "N":
                return "W"

        elif moves == 180:
            if current_direction == "E":
                return "W"
            elif current_direction == "S":
                return "N"
            elif current_direction == "W":
                return "E"
            elif current_direction == "N":
                return "S"

        elif moves == 270:
            if current_direction == "E":
                return "S"
            elif current_direction == "S":
                return "W"
            elif current_direction == "W":
                return "N"
            elif current_direction == "N":
                return "E"

def get_coordinates(path:str)->dict:

    x, y = 0, 0
    current_direction = "E"

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():

            action = line[0]
            moves = int(line[1:])

            if action == "F":
                x, y = move_in_current_direction(moves, current_direction, x, y)
            elif action == "N" or action == "S" or action == "E" or action == "W":
                x, y = shift_in_current_direction(action, moves, x, y)
            elif action == "L" or action == "R":
                current_direction = change_direction(current_direction, action, moves)

            # print(x, y)

    return x, y

def move_in_current_direction2(moves, current_direction, x, y, way_x, way_y):

    x = x + way_x * moves
    y = y + way_y * moves

    return x,y

def move_waypoint(action, moves, way_x, way_y):

    if action == "N":
        way_y = way_y  + moves
    elif action == "S":
        way_y = way_y - moves
    elif action == "E":
        way_x = way_x + moves
    elif action == "W":
        way_x = way_x - moves

    return way_x, way_y

def make_turn(direction, way_x, way_y):

    '''
    to make turn we just need to swap coordinates

    e.g.:
    start x:y
    10:1

    turn right 90
    1:-10
    turn right 90
    -10:-1
    and so on

    turn left 90:
    -1:10
    turn left 90:
    -10:-1
    and so on
    '''

    if direction == "R":
        return way_y, -way_x
    else:
        return -way_y, way_x

def change_waypoint_direction(action, moves, way_x, way_y):

    num_of_turns = moves//90

    for turn in range(1,num_of_turns+1):
        way_x, way_y = make_turn(action, way_x, way_y)

    return way_x, way_y

def get_coordinates2(path:str)->dict:

    x, y = 0, 0
    way_x, way_y = 10, 1
    current_direction = "E"

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():

            action = line[0]
            moves = int(line[1:])

            if action == "F":
                x, y = move_in_current_direction2(moves, current_direction, x, y, way_x, way_y)
            elif action == "N" or action == "S" or action == "E" or action == "W":
                way_x, way_y = move_waypoint(action, moves, way_x, way_y)
            elif action == "L" or action == "R":
                way_x, way_y = change_waypoint_direction(action, moves, way_x, way_y)

            print(f"{x}, {y}")
            print(f"waypoint:{way_x},{way_y}")


    return x, y

#Part 1
# x, y = get_coordinates("./test_input.txt")
x, y = get_coordinates("./input.txt")
print(x,y)
print(abs(x)+abs(y))

#Part 2
# x, y = get_coordinates2("./test_input.txt")
x2, y2 = get_coordinates2("./input.txt")
print(x2,y2)
print(abs(x2)+abs(y2))