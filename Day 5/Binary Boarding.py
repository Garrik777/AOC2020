
from pathlib import Path

class Node():
    def __init__(self, seats = None):
        self.seats = seats
        self.f = None
        self.b = None

    def __repr__(self):
        return f"{self.seats}"

def init_tree(node):

    left_row = node.seats[0]
    right_row = node.seats[len(node.seats)-1]
    medium = (right_row + left_row) // 2

    # print(node)

    if left_row != right_row:
        node.f = init_tree(Node([left_row,medium]))
        node.b = init_tree(Node([medium+1,right_row]))
    else:
        return Node([left_row,right_row])

    return node

def get_row_number(path:str, tree:Node)->int:

    for char in path:
        if char == "F":
            tree = tree.f
        else:
            tree = tree.b

    return tree.seats[0]

def get_seat_number(path:str, tree:Node)->int:

    for char in path:
        if char == "L":
            tree = tree.f
        else:
            tree = tree.b

    return tree.seats[0]

def get_highest_id(txt_file)->int:
    rows_tree = init_tree(Node([0, 127]))
    col_tree = init_tree(Node([0, 7]))
    highest_id = 0

    with txt_file.open('r') as f:
        for line in f.readlines():
            raw_line = line.replace('\n', '')
            row_number = get_row_number(raw_line[:7], rows_tree)
            col_number = get_seat_number(raw_line[7:], col_tree)

            cur_id = row_number * 8 + col_number

            if cur_id > highest_id:
                highest_id = cur_id

    return highest_id

def get_my_id(txt_file)->int:
    rows_tree = init_tree(Node([0, 127]))
    col_tree = init_tree(Node([0, 7]))

    ids = set()
    seats = set()

    with txt_file.open('r') as f:
        for line in f.readlines():
            raw_line = line.replace('\n', '')
            row_number = get_row_number(raw_line[:7], rows_tree)
            col_number = get_seat_number(raw_line[7:], col_tree)

            ids.add(row_number * 8 + col_number)
            # seats.add((row_number,col_number))

    ids = list(ids)
    ids.sort()
    # print(ids)
    # print_seats(seats)

    prev_id = ids[0]
    for id in ids[1:]:
        if id - prev_id > 1:
            return prev_id+1
        prev_id = id

def print_seats(seats):

    seats = list(seats)
    seats.sort()

    prev_row = seats[0][0]
    for row in seats:
        if row[0] != prev_row:
            print()
            print(row, end='')
            prev_row = row[0]
        else:
            print(row, end='')


# txt_file = Path("./test_input.txt")
txt_file = Path("./input.txt")

highest_id = get_highest_id(txt_file)
print(highest_id)
my_id = get_my_id(txt_file)
print(my_id)

