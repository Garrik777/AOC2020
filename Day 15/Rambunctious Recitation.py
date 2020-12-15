
from pathlib import Path

def read_input(path:str)->dict:

    turns = []

    txt_file = Path(path)

    with txt_file.open('r') as f:

        input = [line.replace("\n","")  for line in f.readlines()]
        input = input[0].split(",")

        for turn in range(len(input)):
            turns.append((turn+1, int(input[turn])))

    return turns

def calculate_turn(turns, final_turn):

    number = 0
    turn = len(turns)+1

    while turn <= final_turn:

        last_elem = turns.pop()
        last_turn = last_elem[0]
        last_num = last_elem[1]

        number_was_spoken = [index for (index, turn) in enumerate(turns) if turn[1] == last_num]

        if not number_was_spoken:
            turns.append((last_turn, last_num))
            turns.append((turn, 0))
        else:
            earlier_elem = turns.pop(number_was_spoken[0])
            earlier_turn = earlier_elem[0]
            number = turn - 1 - earlier_turn
            turns.append((last_turn, last_num))
            turns.append((turn,number))

        turn += 1

    return number

# turns = read_input("./test_input2.txt")
turns = read_input("./input.txt")
# print(turns)

number = calculate_turn(turns, 2020)
print(number)

number2 = calculate_turn(turns, 30000000)
print(number2)
