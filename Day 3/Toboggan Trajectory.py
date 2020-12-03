
from pathlib import Path

def read_input(path:str):

    txt_file = Path(path)
    if not txt_file.is_file():
        return []

    path_grid = []
    vert_steps = 0


    with txt_file.open('r') as f:
        for line in f.readlines():

            raw_line = tuple(line.replace('\n', ''))
            path_grid.append(raw_line)


            vert_steps += 1
            hor_steps = len(raw_line)
        # vert_steps -= 1 #we are starting from 0-0 pos

        # print(vert_steps, hor_steps)

    return path_grid, hor_steps-1, vert_steps-1

path_grid, hor_steps, vert_steps = read_input("./input.txt")

x = 0
y = 0

counter = 0

while True:

    x += 3
    y += 1

    if x > hor_steps:
        x = x- 1 - hor_steps
        first_grid = False

    if y > vert_steps:
        break

    cur_point = path_grid [y][x]

    if cur_point == "#":
        print(x+1, y+1)
        counter += 1

print(counter)
