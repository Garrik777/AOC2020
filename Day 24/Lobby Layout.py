from pathlib import Path

class Tile():
    def __init__(self,x=0,y=0,color="white"):
        self.x = x
        self.y = y
        self.color = color
    def __repr__(self):
        return f"{self.color}:{self.x},{self.y}"

directions = {
    "nw":(-1,1),
    "w":(-1,0),
    "sw":(-1,-1),
    "se":(1,-1),
    "e":(1,0),
    "ne":(1,1)
}

# Part 1

def get_steps(line):

    steps = []


    while line:

        ind = 0

        if line[ind] == "e":
            steps.append(directions["e"])
            ind +=1
        elif line[ind] == "w":
            steps.append(directions["w"])
            ind +=1
        elif line[ind:ind+2] == "nw":
            steps.append(directions["nw"])
            ind +=2
        elif line[ind:ind+2] == "sw":
            steps.append(directions["sw"])
            ind +=2
        elif line[ind:ind+2] == "se":
            steps.append(directions["se"])
            ind +=2
        elif line[ind:ind+2] == "ne":
            steps.append(directions["ne"])
            ind +=2

        line = line[ind:]
        continue

    return steps

def count_black_tiles(tiles):

    res = [tile for tile in tiles if tile.color == "black"]
    return len(res)

def get_coords(raw_line):

    # odd rows right
    # https://www.redblobgames.com/grids/hexagons/

    cur_x = 0
    cur_y = 0

    steps = get_steps(raw_line)

    for step in steps:
        x, y = step

        #if cur_y is even and next step to the one of left direction
        #then we are changing both coords

        if cur_y%2==0 and x<0:
            n_x = cur_x + x
            n_y = cur_y + y
        elif cur_y%2==0  and x>0:
            if y==0:
                n_x = cur_x + x
                n_y = cur_y + y
            else:
                n_x = cur_x
                n_y = cur_y + y
        elif cur_y%2!=0 and x>0:
            n_x = cur_x + x
            n_y = cur_y + y
        elif cur_y%2!=0 and x<0:
            if y==0:
                n_x = cur_x + x
                n_y = cur_y + y
            else:
                n_x = cur_x
                n_y = cur_y + y

        cur_x = n_x
        cur_y = n_y

    return cur_x, cur_y

def flip_last_tile(path):

    tiles = []
    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():
            raw_line = line.replace("\n", "")

            cur_x, cur_y =  get_coords(raw_line)

            # searching for existing tile
            tile_ind = next((ind for ind, item in enumerate(tiles) if item.x == cur_x and item.y == cur_y), None)

            if tile_ind == None:
                # new_tile = {(cur_x,cur_y):"white"}
                new_tile = Tile(cur_x, cur_y,"black")
                tiles.append(new_tile)
            else:
                if tiles[tile_ind].color == "white":
                    tiles[tile_ind].color = "black"
                else:
                    tiles[tile_ind].color = "white"

    return tiles

tiles = flip_last_tile("./input.txt")
print(count_black_tiles(tiles))

# Part 2

def get_one_adj_coord(x, y, cur_x, cur_y):

    if cur_y%2==0 and x<0:
        cur_x = cur_x + x
        cur_y = cur_y + y
    elif cur_y%2==0  and x>0:
        if y==0:
            cur_x = cur_x + x
            cur_y = cur_y + y
        else:
            cur_x = cur_x
            cur_y = cur_y + y
    elif cur_y%2!=0 and x>0:
        cur_x = cur_x + x
        cur_y = cur_y + y
    elif cur_y%2!=0 and x<0:
        if y==0:
            cur_x = cur_x + x
            cur_y = cur_y + y
        else:
            cur_x = cur_x
            cur_y = cur_y + y

    return cur_x, cur_y

def get_adj_coords(tile):

    adj_coords = []

    for step in directions.values():
        x, y = step
        cur_x, cur_y = get_one_adj_coord(x, y, tile.x, tile.y)
        adj_coords.append((cur_x, cur_y))

    return adj_coords

def flip_all_tiles(tiles):

    white_tiles = {}
    black_tiles = []

    for tile in tiles:

        if tile.color == "white":
            continue

        adj_coords = get_adj_coords(tile)

        black = 0
        for adj_coord in adj_coords:
            cur_x, cur_y = adj_coord
            tile_ind = next((ind for ind, item in enumerate(tiles) if item.x == cur_x and item.y == cur_y and
                             item.color == "black"), None)

            if tile_ind != None:
                black += 1
            else:
                if white_tiles.get((cur_x, cur_y)) != None:
                    white_tiles[(cur_x, cur_y)] +=1
                else:
                    white_tiles[(cur_x, cur_y)] = 1

        if black == 1 or black == 2:
            black_tiles.append(tile)

    for key, item in white_tiles.items():
        if item == 2:
            x,y = key
            black_tiles.append(Tile(x,y, "black"))

    return black_tiles

def flip_tiles_by_days(tiles, days):

    for day in range(1,days+1):
        tiles = flip_all_tiles(tiles)

    return tiles

tiles = flip_last_tile("./input.txt")
res = flip_tiles_by_days(tiles, 100)
black_tiles = count_black_tiles(res)
print(black_tiles)
