from pathlib import Path
from pprint import pprint
from collections import defaultdict

def read_input(path:str)->dict:

    cubes = {}

    x,y,z = 0,0,0

    txt_file = Path(path)

    with txt_file.open('r') as f:

        for line in f.readlines():

            raw_line = line.replace("\n","")

            for char in raw_line:
                if char == ".":
                    continue
                # cubes.append(Cube(char, x,y,z))
                cubes[(x,y,z)] = char
                x += 1

            x = 0
            y += 1

    return cubes

def cycle(cubes):

    new_cubes = defaultdict(int)


    for coord in cubes.keys():

        x = coord[0]
        y = coord[1]
        z = coord[2]

        for x_c in [-1, 0, 1]:
            for y_c in [-1, 0, 1]:
                for z_c in [-1, 0, 1]:

                    if x_c == y_c == z_c == 0:
                        continue

                    new_cubes[(x+x_c,y+y_c,z+z_c)] +=1

    cubes_copy = {}

    for cube in new_cubes:
        if cube not in cubes and new_cubes[cube] == 3:
            cubes_copy[cube] = "#"
        elif cube in cubes and new_cubes[cube] in (2, 3):
            cubes_copy[cube] = "#"

    return cubes_copy

def run_cycles(cubes, number_of_cycles):

    for _ in range(number_of_cycles):
        cubes = cycle(cubes)

    return len(cubes)

def read_input2(path:str)->dict:

    cubes = {}

    x,y,z,w = 0,0,0,0

    txt_file = Path(path)

    with txt_file.open('r') as f:

        for line in f.readlines():

            raw_line = line.replace("\n","")

            for char in raw_line:
                if char == ".":
                    continue
                # cubes.append(Cube(char, x,y,z))
                cubes[(x,y,z,w)] = char
                x += 1

            x = 0
            y += 1

    return cubes

def cycle2(cubes):
    new_cubes = defaultdict(int)

    for coord in cubes.keys():

        x = coord[0]
        y = coord[1]
        z = coord[2]
        w = coord[3]

        for x_c in [-1, 0, 1]:
            for y_c in [-1, 0, 1]:
                for z_c in [-1, 0, 1]:
                    for w_c in [-1, 0, 1]:

                        if x_c == y_c == z_c == w_c = 0:
                            continue

                        new_cubes[(x + x_c, y + y_c, z + z_c, w + w_c)] += 1

    cubes_copy = {}

    for cube in new_cubes:
        if cube not in cubes and new_cubes[cube] == 3:
            cubes_copy[cube] = "#"
        elif cube in cubes and new_cubes[cube] in (2, 3):
            cubes_copy[cube] = "#"

    return cubes_copy

def run_cycles2(cubes, number_of_cycles):

    for _ in range(number_of_cycles):
        cubes = cycle(cubes)

    return len(cubes)

initial_state = read_input("./input.txt")
pprint(initial_state)

# first_run = cycle(initial_state)
# pprint(first_run)

cubes = run_cycles(initial_state, 6)
pprint(cubes)

initial_state = read_input2("./input.txt")
pprint(initial_state)

cubes = run_cycles2(initial_state, 6)
pprint(cubes)


