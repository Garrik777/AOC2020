from pprint import pprint
from pathlib import Path
import copy

def read_input(path:str)->list:

    seats = []

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():

            # raw_line = line.replace('\n', '')
            #
            # row = []
            # for char in raw_line:
            row = [char for char in line.replace('\n', '')]

            seats.append(row)

    return seats

def check_seat(grid:list, y:int, x:int)->str:

    current_condition = grid[y] [x]
    if current_condition == ".":
        return "."

    start_x = max(x-1, 0)
    start_y = max(y-1, 0)

    fin_x = min(x+1, len(grid[0])-1)
    fin_y = min(y+1, len(grid)-1)

    cur_x = start_x
    cur_y = start_y

    number_of_occupied = 0

    while cur_y <= fin_y:


        while cur_x <= fin_x:

            #exclude current coordinate
            if cur_x == x and cur_y == y:
                cur_x += 1
                continue

            value = grid[cur_y] [cur_x]

            if value == "#":
                number_of_occupied += 1

            cur_x += 1

        cur_y += 1
        cur_x = start_x


    if current_condition == "L" and not number_of_occupied:
        return "#"
    elif  current_condition == "#" and  number_of_occupied >= 4:
        return "L"
    else:
        return current_condition

def get_stable_layout(seats:list)->list:

    rows = len(seats)
    seats_in_row = len(seats[0])

    current_layout = copy.deepcopy(seats)
    prev_layout = copy.deepcopy(seats)

    seat_changed= True

    while seat_changed:
        seat_changed = False
        prev_layout = copy.deepcopy(current_layout)
        for row in range(rows):
            for seat in range(seats_in_row):
                cur_condition = current_layout[row][seat]
                current_layout[row][seat] = check_seat(prev_layout, row, seat)

                if cur_condition != current_layout[row][seat]:
                    seat_changed = True

        # pprint(current_layout)

    return current_layout

def count_occupied_seats(seats:list)->int:

    counter = 0

    for row in seats:
        for seat in row:
            if seat == "#":
                counter += 1

    return counter

def check_seat_direction(grid:list, y:int, x:int)->str:

    '''
    Now we need to check
    the first seat they can see in each of  eight directions!

    So we need to analyse all grid in a worst case
    '''

    current_condition = grid[y] [x]
    if current_condition == ".":
        return "."

    start_x = 0
    fin_x = len(grid[0]) - 1

    start_y = 0
    fin_y = len(grid)-1

    cur_x = x
    cur_y = y

    number_of_occupied = 0

    # x axis check to the left
    cur_x -= 1
    while cur_x >= start_x:
        value = grid[cur_y][cur_x]

        if value == "#":
            number_of_occupied += 1
            break
        elif value == "L":
            break

        cur_x -= 1

    # x axis check to the right
    cur_x = x+1
    while cur_x <= fin_x:
        value = grid[cur_y][cur_x]

        if value == "#":
            number_of_occupied += 1
            break
        elif value == "L":
            break

        cur_x += 1

    # y axis check to the up
    cur_x = x
    cur_y -= 1
    while cur_y >= start_y:
        value = grid[cur_y][cur_x]

        if value == "#":
            number_of_occupied += 1
            break
        elif value == "L":
            break

        cur_y -= 1

    # y axis check to the bottom
    cur_x = x
    cur_y = y+1
    while cur_y <= fin_y:
        value = grid[cur_y][cur_x]

        if value == "#":
            number_of_occupied += 1
            break
        elif value == "L":
            break

        cur_y += 1

    #diagonal left top
    cur_x = x-1
    cur_y = y-1
    while cur_x >= start_x and cur_y >= start_y:

        value = grid[cur_y][cur_x]

        if value == "#":
            number_of_occupied += 1
            break
        elif value == "L":
            break

        cur_x -= 1
        cur_y -= 1

    # diagonal left bottom
    cur_x = x - 1
    cur_y = y + 1
    while cur_x >= start_x and cur_y <= fin_y:

        value = grid[cur_y][cur_x]

        if value == "#":
            number_of_occupied += 1
            break
        elif value == "L":
            break

        cur_x -= 1
        cur_y += 1

    # diagonal right top
    cur_x = x + 1
    cur_y = y - 1
    while cur_x <= fin_x and cur_y >= start_y:

        value = grid[cur_y][cur_x]

        if value == "#":
            number_of_occupied += 1
            break
        elif value == "L":
            break

        cur_x += 1
        cur_y -= 1

    # diagonal right bottom
    cur_x = x + 1
    cur_y = y + 1
    while cur_x <= fin_x and cur_y <= fin_y:

        value = grid[cur_y][cur_x]

        if value == "#":
            number_of_occupied += 1
            break
        elif value == "L":
            break

        cur_x += 1
        cur_y += 1

    if current_condition == "L" and not number_of_occupied:
        return "#"
    elif  current_condition == "#" and  number_of_occupied >= 5:
        return "L"
    else:
        return current_condition

def get_stable_layout2(seats:list)->list:

    rows = len(seats)
    seats_in_row = len(seats[0])

    current_layout = copy.deepcopy(seats)
    prev_layout = copy.deepcopy(seats)

    seat_changed= True

    while seat_changed:
        seat_changed = False
        prev_layout = copy.deepcopy(current_layout)
        for row in range(rows):
            for seat in range(seats_in_row):
                cur_condition = current_layout[row][seat]
                current_layout[row][seat] = check_seat_direction(prev_layout, row, seat)

                if cur_condition != current_layout[row][seat]:
                    seat_changed = True

        # pprint(current_layout)

    return current_layout


# seats = read_input("./test_input.txt")
seats = read_input("./input.txt")
# pprint(seats)

# Part 1

stable_layout = get_stable_layout(seats)
# pprint(stable_layout)

occupied_seats = count_occupied_seats(stable_layout)
pprint(occupied_seats)

# Part 2

stable_layout2 = get_stable_layout2(seats)
pprint(count_occupied_seats(stable_layout2))


