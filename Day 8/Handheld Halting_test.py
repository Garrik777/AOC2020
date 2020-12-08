from pathlib import Path
from pprint import pprint

def read_input(path:str)->list:

    code_lines = []
    index = 0

    txt_file = Path(path)

    with txt_file.open('r') as f:
        for line in f.readlines():

            raw_line = line.replace('\n', '')
            code_lines.append(raw_line)

    return code_lines

def execute_code(code_lines:list)->int:

    code_len = len(code_lines)-1
    accum = 0
    cur_index = 0
    line = code_lines[cur_index]
    executed_lines = {}

    while True:

        current_line = line.split(" ")
        action = current_line[0]
        move = int(current_line[1])

        if executed_lines.get(cur_index) != None:
            break
        executed_lines[cur_index] = cur_index

        if action == "nop":
            cur_index += 1
        elif action == "acc":
            accum += move
            cur_index += 1
        elif action == "jmp":
            cur_index += move

        if cur_index > code_len:
            return accum
        else:
            line = code_lines[cur_index]

    return accum

#checks modified code for execution
def check_code(code_lines:list)->bool:

    code_len = len(code_lines)-1
    accum = 0
    cur_index = 0
    lowest_index = 0
    line = code_lines[cur_index]
    executed_lines = {}

    while True:

        current_line = line.split(" ")
        action = current_line[0]
        move = int(current_line[1])

        if executed_lines.get(cur_index) != None:
            return False #can't get to the end of the code

        executed_lines[cur_index] = current_line

        if cur_index > lowest_index:
            lowest_index = cur_index

        if action == "nop":
            cur_index += 1
        elif action == "acc":
            accum += move
            cur_index += 1
        elif action == "jmp":
            cur_index += move

        if cur_index > code_len:
            return True
        else:
            line = code_lines[cur_index]

    return True

def get_executed_lines(code_lines:list)->int:

    code_len = len(code_lines)-1
    cur_index = 0
    lowest_index = 0
    line = code_lines[cur_index]
    executed_lines = {}

    while True:

        current_line = line.split(" ")
        action = current_line[0]
        move = int(current_line[1])

        if executed_lines.get(cur_index) != None:
            return executed_lines

        executed_lines[cur_index] = current_line

        if cur_index > lowest_index:
            lowest_index = cur_index

        if action == "nop":
            cur_index += 1
            line = code_lines[cur_index]
        elif action == "acc":
            cur_index += 1
            line = code_lines[cur_index]
        elif action == "jmp":
            cur_index += move
            line = code_lines[cur_index]

        if cur_index > code_len:
            return executed_lines
        else:
            line = code_lines[cur_index]


    return executed_lines

def find_correct_code(executed_lines:list, code_lines:list)->int:

    acc = 0

    for index in executed_lines:

        code_lines_copy = code_lines.copy()
        action = executed_lines[index][0]

        if action == "acc":
            continue

        code_line = code_lines[index]

        if action == "jmp":
            code_line = code_line.replace("jmp","nop")
        elif action == "nop":
            code_line = code_line.replace("nop","jmp")

        code_lines_copy[index] = code_line

        result = check_code(code_lines_copy)

        if result:
            # print(executed_lines[index])
            acc = execute_code(code_lines_copy)
            # print(acc)
            return acc

        # print(index, action)


# code_lines = read_input("./test_input.txt")
code_lines = read_input("./input.txt")
# pprint(code_lines)

acc = execute_code(code_lines)
pprint(acc)

executed_lines = get_executed_lines(code_lines)
# pprint(executed_lines)
acc2 = find_correct_code(executed_lines, code_lines)
pprint(acc2)


