
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

def trees_count(path_grid, hor_steps, vert_steps, step_right, step_down):

    x = 0
    y = 0

    counter = 0

    while True:

        x += step_right
        y += step_down

        if x > hor_steps:
            x = x - 1 - hor_steps

        if y > vert_steps:
            break

        cur_point = path_grid[y][x]

        if cur_point == "#":
            counter += 1

    return counter

path_grid, hor_steps, vert_steps = read_input("./input.txt")

slope1 = trees_count(path_grid, hor_steps, vert_steps, 1,1)
slope2 = trees_count(path_grid, hor_steps, vert_steps, 3,1)
slope3 = trees_count(path_grid, hor_steps, vert_steps, 5,1)
slope4 = trees_count(path_grid, hor_steps, vert_steps, 7,1)
slope5 = trees_count(path_grid, hor_steps, vert_steps, 1,2)

print(slope1, slope2, slope3, slope4, slope5)
