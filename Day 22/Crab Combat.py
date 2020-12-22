from collections import deque
import copy
from pathlib import Path
from pprint import pprint


def read_input(path: str):

    deck1 = deque()
    deck2 = deque()

    reading_deck1 = True

    txt_file = Path(path)

    with txt_file.open('r') as f:

        for line in f.readlines():

            raw_line = line.replace("\n", "")

            if "Player 2:" in raw_line:
                reading_deck1 = False
                continue

            if raw_line == "Player 1:" or raw_line == "":
                continue

            if reading_deck1:
                deck1.append(int(raw_line))
            else:
                deck2.append(int(raw_line))

    return deck1, deck2

def play_game(deck1, deck2):

    while len(deck1) and len(deck2):

        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    return deck1, deck2

def calc_result(deck1, deck2):

    if len(deck1):
        res_deck = deck1
    else:
        res_deck = deck2


    res = 0
    mult =1
    for ind in range(len(res_deck)):
        val = res_deck.pop()

        res += val * mult
        mult += 1

    return res

# Part 1
# deck1, deck2 = read_input("./test_input.txt")
deck1, deck2 = read_input("./input.txt")
deck1, deck2 = play_game(deck1, deck2)
print(calc_result(deck1, deck2))


# Part 2
def get_new_deck(deck, col):
    new_deck = deque()

    for ind in range(col):
        new_deck.append(deck[ind])

    return new_deck

def play_game2(deck1, deck2):

    hash = {}

    while len(deck1) and len(deck2):

        if hash.get(tuple(deck1)) or hash.get(tuple(deck2)):
            return 1
        else:
            hash[tuple(deck1)] = 1
            hash[tuple(deck2)] = 1

        card1 = deck1.popleft()
        card2 = deck2.popleft()


        if card1 <= len(deck1) and card2 <= len(deck2):
            winner = play_game2(get_new_deck(deck1, card1), get_new_deck(deck2, card2))

            if winner == 1:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
            continue

        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    if len(deck1):
        return 1
    else:
        return 2

def calc_result(res_deck):

    res = 0
    mult =1
    for ind in range(len(res_deck)):
        val = res_deck.pop()

        res += val * mult
        mult += 1

    return res

# deck1, deck2 = read_input("./test_input.txt")
# deck1, deck2 = read_input("./test_infinite.txt")
deck1, deck2 = read_input("./input.txt")

# winner = play_game2(copy.deepcopy(deck1), copy.deepcopy(deck2))
winner = play_game2(deck1, deck2)
if winner == 1:
    print(calc_result(deck1))
else:
    print(calc_result(deck2))



