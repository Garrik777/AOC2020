from pathlib import Path
from pprint import pprint
import copy
import math

def tests():
    print("---------flip horizontally tile 1171-------------")
    pprint(tiles[1171])
    fh = flip_hor(tiles[1171])
    pprint(fh)

    print("---------flip vertically tile 1489-------------")
    fv = flip_vert(tiles[1489])
    pprint(tiles[1489])
    pprint(fv)

    print("---------flip horizontally and rotate to the right tile 2473-------------")
    pprint(tiles[2473])
    fh = flip_hor(tiles[2473])
    pprint(fh)
    fh = rotate_right(fh)
    pprint(fh)

    print("---------rotate to the left tile 2971-------------")
    pprint(tiles[2971])
    fv = rotate_left(tiles[2971])
    pprint(fv)


def edge_test(left_tile, right_tile, top_tile, bottom_tile):
    left_tile = flip_vert(left_tile)
    right_tile = flip_vert(right_tile)

    # pprint(left_tile)
    # pprint(right_tile)

    edges_equal = compare_right_left_edge(left_tile, right_tile)
    print(edges_equal)

    top_tile = flip_hor(top_tile)
    top_tile = rotate_right(top_tile)
    bottom_tile = flip_hor(bottom_tile)
    edges_equal = compare_top_bottom_edge(top_tile, bottom_tile)
    print(edges_equal)


def read_input(path: str):
    tiles = {}

    txt_file = Path(path)

    with txt_file.open('r') as f:

        tile = []

        for line in f.readlines():

            raw_line = line.replace("\n", "")

            if "Tile" in raw_line:
                tile_num = raw_line.split(" ")
                tile_num = int(tile_num[1].replace(":", ""))
                continue

            if raw_line == '':
                tiles[tile_num] = tile
                tile = []
            else:
                cur_line = []
                for char in raw_line:
                    cur_line.append(char)
                tile.append(cur_line)

    tiles[tile_num] = tile

    return tiles


def flip_hor(tile):
    return [line[::-1] for line in tile]


def flip_vert(tile):
    return [line for line in tile[::-1]]


def rotate_right(tile):
    # first column becomes first line, second colum- second line and etc

    tile_flipped = []

    for ind in range(len(tile)):
        new_line = [item[ind] for item in tile]
        tile_flipped.append(new_line[::-1])

    return tile_flipped


def rotate_left(tile):
    # last column becomes first line, second from last colum- second line and etc

    tile_flipped = []

    for ind in range(len(tile) - 1, -1, -1):
        new_line = [item[ind] for item in tile]
        tile_flipped.append(new_line)

    return tile_flipped

def compare_right_left_edge(left_tile, right_tile):
    # comparing last and first columns

    tile_len = len(left_tile)

    right_column = [item[tile_len - 1] for item in left_tile]
    left_column = [item[0] for item in right_tile]

    for ind in range(tile_len):

        if right_column[ind] != left_column[ind]:
            return False

    return True

def compare_top_bottom_edge(top_tile, bottom_tile):
    tile_len = len(top_tile)

    top_line = bottom_tile[0]
    bottom_line = top_tile[tile_len - 1]

    for ind in range(len(top_line)):
        if top_line[ind] != bottom_line[ind]:
            return False

    return True

def get_possible_states(tile):
    possible_states = []
    possible_states.append(tile)
    possible_states.append(flip_hor(tile))
    possible_states.append(flip_vert(tile))
    possible_states.append(rotate_right(tile))
    possible_states.append(rotate_left(tile))
    possible_states.append(rotate_right(flip_hor(tile)))
    possible_states.append(rotate_left(flip_hor(tile)))
    possible_states.append(rotate_right(flip_vert(tile)))
    possible_states.append(rotate_left(flip_vert(tile)))

    return possible_states

def init_grid(tiles):

    lenght = len(tiles)
    line_len = int(math.sqrt(lenght))

    line = [0 for item in range(line_len)]
    grid = [line for item in range(line_len)]
    return grid


def check_tiles_test(x,y,grid, tiles, used_tiles, input, tiles_grid):

    if x>2 or y>2:
        return grid

    cur_grid = copy.deepcopy(grid)

    for tile in tiles:

        if x==y==0: #top level
            grid = init_grid(tiles)
            # tiles_grid = init_grid(tiles)
            used_tiles = [tile]

        if x > 0:
            left_tile = cur_grid[y][x-1]
        else:
            left_tile = None

        if y > 0:
            top_tile = cur_grid[y-1][x]
        else:
            top_tile = None

        if x == 2:
            x_next = 0
            y_next = y + 1
        else:
            x_next = x + 1
            y_next = y

        possible_states = get_possible_states(input[tile])



        for state in possible_states:

            if left_tile != None:
                edges_equal = compare_right_left_edge(left_tile, state)
            else:
                edges_equal = True

            if top_tile != None:
                top_equal = compare_top_bottom_edge(top_tile, state)
            else:
                top_equal = True

            if edges_equal and top_equal:
                cur_grid[y][x] = state
                used_tiles.append(tile)
                tiles_grid[y][x] = tile
                res = check_tiles_test(x_next, y_next, cur_grid, [tile for tile in tiles if tile not in used_tiles],
                                  copy.deepcopy(used_tiles), input, tiles_grid)

                if res == None:
                    continue
                else:
                    return res

    return None

def start_test(tiles):

    lenght = len(tiles)
    line_len = int(math.sqrt(lenght))

    # line = [0 for item in range(line_len)]
    # grid = [line for item in range(line_len)]
    # tiles_grid = copy.deepcopy(grid)

    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    tiles_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # for tile in tiles:
    #     grid[0][0] = tiles[tile]
    res = check_tiles_test(0,0,grid,[tile for tile in tiles if tile],[], tiles, tiles_grid)

    pprint(res)
    pprint(tiles_grid)

def check_tiles(x,y,grid, tiles, used_tiles, input, tiles_grid):

    if x>11 or y>11:
        return grid

    cur_grid = copy.deepcopy(grid)

    for tile in tiles:

        if x==y==0: #top level
            cur_grid = init_grid(tiles)
            # tiles_grid = init_grid(tiles)
            used_tiles = [tile]

        if x > 0:
            left_tile = cur_grid[y][x-1]
        else:
            left_tile = None

        if y > 0:
            top_tile = cur_grid[y-1][x]
        else:
            top_tile = None

        if x == 11:
            x_next = 0
            y_next = y + 1
        else:
            x_next = x + 1
            y_next = y

        possible_states = get_possible_states(input[tile])



        for state in possible_states:

            if left_tile != None:
                edges_equal = compare_right_left_edge(left_tile, state)
            else:
                edges_equal = True

            if top_tile != None:
                top_equal = compare_top_bottom_edge(top_tile, state)
            else:
                top_equal = True

            if edges_equal and top_equal:
                cur_grid[y][x] = state
                used_tiles.append(tile)
                tiles_grid[y][x] = tile
                next_tiles = [tile for tile in tiles if tile not in used_tiles]
                res = check_tiles(x_next, y_next, cur_grid, next_tiles,
                                  copy.deepcopy(used_tiles), input, tiles_grid)

                if res == None:
                    continue
                else:
                    return res

    return None

def check_edges(x,y,grid, tiles, used_tiles, input, tiles_grid):

    if x>11 or y>11:
        return grid

    cur_grid = copy.deepcopy(grid)

    for tile in tiles:

        if x==y==0: #top level
            cur_grid = init_grid(tiles)
            # tiles_grid = init_grid(tiles)
            used_tiles = [tile]

            x_next = 1
            y_next = 0

        elif x ==1 and y == 0:
            x_next = 0
            y_next = 1

        elif x ==0 and y == 1:
            x_next = 10
            y_next = 0

        elif x ==10 and y == 0:
            x_next = 11
            y_next = 0

        elif x ==11 and y == 0:
            x_next = 11
            y_next = 1

        elif x ==11 and y == 1:
            x_next = 0
            y_next = 11

        elif x ==0 and y == 11:
            x_next = 1
            y_next = 11

        elif x ==1 and y == 11:
            x_next = 11
            y_next = 10

        elif x ==11 and y == 10:
            x_next = 10
            y_next = 11

        elif x ==10 and y == 11:
            x_next = 11
            y_next = 11

        else:
            return grid

        if x > 0:
            left_tile = cur_grid[y][x-1]
            if not left_tile:
                left_tile = None

        else:
            left_tile = None

        if y > 0:
            top_tile = cur_grid[y-1][x]
            if not top_tile:
                top_tile = None
        else:
            top_tile = None
        #
        # if x == 11:
        #     x_next = 0
        #     y_next = y + 1
        # else:
        #     x_next = x + 1
        #     y_next = y

        possible_states = get_possible_states(input[tile])



        for state in possible_states:

            if left_tile != None:
                edges_equal = compare_right_left_edge(left_tile, state)
            else:
                edges_equal = True

            if top_tile != None:
                top_equal = compare_top_bottom_edge(top_tile, state)
            else:
                top_equal = True

            if edges_equal and top_equal:
                cur_grid[y][x] = state
                used_tiles.append(tile)
                tiles_grid[y][x] = tile
                next_tiles = [tile for tile in tiles if tile not in used_tiles]
                res = check_tiles(x_next, y_next, cur_grid, next_tiles,
                                  copy.deepcopy(used_tiles), input, tiles_grid)

                if res == None:
                    continue
                else:
                    return res

    return None


def start(tiles):

    # grid = init_grid(tiles)
    # tiles_grid = init_grid(tiles)
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    tiles_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    # res = check_tiles(0,0,grid,[tile for tile in tiles if tile],[], tiles, tiles_grid)
    res = check_edges(0,0,grid,[tile for tile in tiles if tile],[], tiles, tiles_grid)
    # res = check_tiles_test(0,0,grid,[tile for tile in tiles if tile],[], tiles, tiles_grid)

    pprint(res)
    pprint(tiles_grid)


# tiles = read_input("./test_input.txt")
# tiles = read_input("./test_input2.txt")
tiles = read_input("./input.txt")
# pprint(tiles)
# print(len(tiles))

# tests()
# start_test(tiles)

start(tiles)